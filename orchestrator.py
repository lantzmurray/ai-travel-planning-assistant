"""Orchestrator for Project 21."""

import os
import sys
from typing import Any, Dict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agents.base import generate_session_id, log_agent_response
from agents.itinerary_builder_agent import build_itinerary
from agents.cost_estimator_agent import estimate_cost
from agents.local_culture_coach_agent import coach_culture
from agents.packing_list_agent import generate_packing_list

AGENT_SEQUENCE = (
    ("Itinerary Builder", build_itinerary),
    ("Cost Estimator", estimate_cost),
    ("Local Culture Coach", coach_culture),
    ("Packing List Generator", generate_packing_list),
)


import concurrent.futures

class Orchestrator:
    """Coordinate the trip-planning specialists in a simple fixed pipeline."""

    def generate_session_id(self) -> str:
        return generate_session_id()

    def run_workflow(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        session_id = self.generate_session_id()
        results = {}

        log_agent_response(
            session_id,
            "Workflow Input",
            "\n".join(
                f"- {key.replace('_', ' ').title()}: {value or 'Not provided'}"
                for key, value in inputs.items()
            ),
            {"kind": "input"},
        )

        with concurrent.futures.ThreadPoolExecutor() as executor:
            future_to_agent = {
                executor.submit(agent_runner, session_id, inputs): agent_name
                for agent_name, agent_runner in AGENT_SEQUENCE
            }
            for future in concurrent.futures.as_completed(future_to_agent):
                agent_name = future_to_agent[future]
                results[agent_name] = future.result()

        return {"session_id": session_id, "results": results}
