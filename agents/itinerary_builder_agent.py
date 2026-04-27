"""Itinerary builder agent for Project 21."""

from agents.base import run_agent_task


def build_itinerary(session_id: str, context_data: dict) -> str:
    """Build a travel flow that can be demoed without pretending bookings exist."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Itinerary Builder",
        context_data=context_data,
        objective=(
            "Create a practical trip outline that matches the destination, "
            "budget, and interests supplied by the user."
        ),
        sections=[
            "Trip arc",
            "Day-by-day itinerary",
            "Book-first checklist",
        ],
        extra_guidance=(
            "Do not fabricate confirmed reservations. Suggest a realistic order "
            "of planning and clearly label any assumptions about trip length."
        ),
    )
