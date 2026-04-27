"""Cost estimator agent for Project 21."""

from agents.base import run_agent_task


def estimate_cost(session_id: str, context_data: dict) -> str:
    """Break the trip into useful cost buckets and tradeoffs."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Cost Estimator",
        context_data=context_data,
        objective=(
            "Estimate the likely cost buckets for the trip and show the user "
            "where they can spend more or save money."
        ),
        sections=[
            "Budget snapshot",
            "Biggest cost drivers",
            "Savings levers",
        ],
        extra_guidance=(
            "Use ranges instead of fake exact prices. Make the budget logic easy "
            "to explain in a walkthrough."
        ),
    )
