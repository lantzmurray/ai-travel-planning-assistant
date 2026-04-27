"""Smoke tests for the Project 21 travel planning workflow."""

from unittest import TestCase, mock

import orchestrator
from agents.packing_list_agent import generate_packing_list


class OrchestratorWorkflowTests(TestCase):
    """Verify the merged workflow shape without calling a live model."""

    def test_agent_sequence_includes_packing_list_generator(self) -> None:
        self.assertEqual(
            [name for name, _ in orchestrator.AGENT_SEQUENCE],
            [
                "Itinerary Builder",
                "Cost Estimator",
                "Local Culture Coach",
                "Packing List Generator",
            ],
        )

    def test_run_workflow_collects_outputs_for_each_agent(self) -> None:
        fake_sequence = (
            ("Itinerary Builder", lambda session_id, inputs: "itinerary"),
            ("Cost Estimator", lambda session_id, inputs: "budget"),
            ("Local Culture Coach", lambda session_id, inputs: "culture"),
            ("Packing List Generator", lambda session_id, inputs: "packing"),
        )

        with (
            mock.patch.object(orchestrator, "AGENT_SEQUENCE", fake_sequence),
            mock.patch.object(orchestrator, "generate_session_id", return_value="abc12345"),
            mock.patch.object(orchestrator, "log_agent_response"),
        ):
            workflow = orchestrator.Orchestrator().run_workflow(
                {
                    "destination": "Kyoto, Japan",
                    "travel_dates": "Late November for a 5-day trip",
                    "budget": "Moderate",
                    "interests": "Temples, food, and quiet gardens",
                }
            )

        self.assertEqual(workflow["session_id"], "abc12345")
        self.assertEqual(
            workflow["results"],
            {
                "Itinerary Builder": "itinerary",
                "Cost Estimator": "budget",
                "Local Culture Coach": "culture",
                "Packing List Generator": "packing",
            },
        )


class PackingListAgentTests(TestCase):
    """Verify the merged agent is wired through the shared runtime helper."""

    def test_generate_packing_list_uses_runtime_helper(self) -> None:
        context = {
            "destination": "Kyoto, Japan",
            "travel_dates": "Late November",
            "interests": "Temples and markets",
        }

        with mock.patch("agents.packing_list_agent.run_agent_task", return_value="ok") as runner:
            result = generate_packing_list("abc12345", context)

        self.assertEqual(result, "ok")
        runner.assert_called_once()
        self.assertEqual(runner.call_args.kwargs["agent_name"], "Packing List Generator")
        self.assertEqual(runner.call_args.kwargs["context_data"], context)
