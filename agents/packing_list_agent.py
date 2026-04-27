"""Packing list agent for Project 21."""

from agents.base import run_agent_task


def generate_packing_list(session_id: str, context_data: dict) -> str:
    """Turn trip details into a practical, category-based packing checklist."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Packing List Generator",
        context_data=context_data,
        objective=(
            "Create a practical packing list that matches the destination, "
            "travel dates, and planned activities."
        ),
        sections=[
            "Weather assumptions",
            "Core packing checklist",
            "Activity-specific extras",
        ],
        extra_guidance=(
            "Group the list into clear categories, keep it realistic for carry-on "
            "friendly travel when possible, and call out any destination-specific "
            "items that matter."
        ),
    )
