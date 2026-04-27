"""Local culture coach agent for Project 21."""

from agents.base import run_agent_task


def coach_culture(session_id: str, context_data: dict) -> str:
    """Surface etiquette and context that make the plan feel grounded."""
    return run_agent_task(
        session_id=session_id,
        agent_name="Local Culture Coach",
        context_data=context_data,
        objective=(
            "Highlight local etiquette, pacing, and cultural context that will "
            "help the traveler navigate the destination respectfully."
        ),
        sections=[
            "Cultural expectations",
            "Common traveler mistakes to avoid",
            "Helpful customs or phrases",
        ],
        extra_guidance=(
            "Prefer respectful, practical guidance over stereotypes. If the "
            "destination is broad, call out that the advice is high level."
        ),
    )
