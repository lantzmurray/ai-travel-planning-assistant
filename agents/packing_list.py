"""
Packing List Generator - Create trip-appropriate packing lists.

ROLE:
Generate comprehensive packing lists based on destination,
weather, trip duration, and activities.
"""

from agents.base import call_llm


def generate_packing_list(destination: str, dates: str = "",
                         interests: list = None) -> str:
    """
    Generate a packing list for a trip.

    Args:
        destination: Travel destination
        dates: Travel dates
        interests: List of activity interests

    Returns:
        Formatted packing list
    """
    interest_str = ", ".join(interests) if interests else "general sightseeing"

    prompt = f"""Generate a packing list for a trip to {destination}.

Dates: {dates if dates else "Flexible"}
Activities: {interest_str}

Include:
1. CLOTHING (appropriate for weather and activities)
2. TOILETRIES (travel-size essentials)
3. ELECTRONICS (chargers, adapters)
4. DOCUMENTS (passport, tickets, reservations)
5. COMFORT ITEMS (neck pillow, earplugs, etc.)
6. ACTIVITY-SPECIFIC (hiking shoes, formal wear, etc.)

Organize by category.
Keep it practical - don't overpack.
Label any items that might be destination-specific.
"""

    return call_llm(prompt)


def get_weather_based_packing(destination: str, month: str = "") -> Dict:
    """
    Get weather-based packing recommendations.

    Returns:
        Dict with weather info and clothing suggestions
    """
    prompt = f"""What should I pack for {destination} in {month if month else "general"}?

Consider:
1. Typical weather (temperature, rain, humidity)
2. Clothing layers needed
3. Special items (umbrella, sun protection, etc.)
4. What NOT to pack (bulky items available there)

Return as organized bullet points by category.
"""

    result = call_llm(prompt)

    return {
        "destination": destination,
        "month": month,
        "recommendations": result
    }