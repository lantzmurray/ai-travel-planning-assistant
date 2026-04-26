"""
PROJECT 21: Travel Planning Assistant

PURPOSE:
AI-powered travel planning - research destinations, create itineraries,
budget trips, and organize travel details.

CORE CONCEPT:
- Input: destination, dates, budget, preferences
- Research: attractions, restaurants, hotels, transportation
- Output: Day-by-day itinerary with costs

PROJECT 14 SIMILARITIES:
- Same agent architecture
- TinyDB logging
- Timeline visualization

NEW COMPONENTS:
- destination_researcher.py: Research destinations
- itinerary_builder.py: Create day-by-day plans
- budget_calculator.py: Estimate and track costs
- booking_helper.py: Format booking links/info
- packing_list.py: Generate packing lists

FILE STRUCTURE:
soai-21-travelplanner/
├── agents/
│   ├── __init__.py
│   ├── base.py              # LLM calls, TinyDB logging
│   ├── destination_researcher.py  # NEW: Research places
│   ├── itinerary_builder.py  # NEW: Build itineraries
│   ├── budget_calculator.py  # NEW: Cost estimation
│   ├── booking_helper.py     # NEW: Booking links
│   ├── packing_list.py      # NEW: Packing lists
│   ├── timeline_builder.py
│   └── visualizer.py
├── orchestrator.py
├── frontend.py
└── requirements.txt
"""

# ============================================================================
# TODO 1: DESTINATION RESEARCHER (agents/destination_researcher.py)
# ============================================================================
# Research destinations for travel planning.
#
# """
# Destination Researcher - Gather info about travel destinations.
#
# ROLE:
# Research attractions, restaurants, hotels, weather, culture
# for a given destination and travel dates.
#
# RESEARCH AREAS:
# - Top attractions and activities
# - Restaurant recommendations
# - Hotel areas and options
# - Local customs and tips
# - Weather expectations
# - Transportation options
# """
#
# from agents.base import call_llm
# from typing import Dict, List
#
# def research_destination(destination: str, dates: str = "",
#                          purpose: str = "tourism") -> Dict:
#     """
#     Research a destination comprehensively.
#
#     Args:
#         destination: City, country, or region
#         dates: Travel dates (optional)
#         purpose: tourism, business, family, romantic
#
#     Returns:
#         Dict with research findings
#     """
#     prompt = f"""Research {destination} for travel planning.
#
# Travel Dates: {dates if dates else "Dates not specified"}
# Purpose: {purpose}
#
# Provide research on:
# 1. TOP ATTRACTIONS (5-7 must-see places with brief descriptions)
# 2. BEST AREAS TO STAY (neighborhoods with character)
# 3. RESTAURANT TYPES (local cuisine, price ranges, specific recommendations)
# 4. TRANSPORTATION (from airport, around city)
# 5. LOCAL TIPS (customs, etiquette, safety, money)
# 6. WEATHER (what to expect)
# 7. ESTIMATED COSTS (daily budget - budget/midrange/luxury)
#
# Be specific and practical. Use real place names.
# """
#
#     return call_llm(prompt)
#
# def get_attraction_details(attraction: str, destination: str) -> Dict:
#     """
#     Get detailed info about a specific attraction.
#
#     Args:
#         attraction: Attraction name
#         destination: City/country
#
#     Returns:
#         Dict with details
#     """
#     prompt = f"""Get details about visiting {attraction} in {destination}:
#
# Include:
# 1. What it is and why it's worth visiting
# 2. Typical hours and best time to visit
# 3. Estimated visit duration
# 4. Ticket prices (if applicable)
# 5. Tips for visiting (avoid crowds, combo tickets, etc.)
# 6. Accessibility notes
# """
#
#     details = call_llm(prompt)
#
#     return {
#         "attraction": attraction,
#         "destination": destination,
#         "details": details
#     }
#
# def find_local_food(destination: str, cuisine_type: str = "",
#                    price_range: str = "midrange") -> List[Dict]:
#     """
#     Find restaurant recommendations.
#
#     Args:
#         destination: City/country
#         cuisine_type: Specific cuisine or empty for local
#         price_range: budget/midrange/luxury
#
#     Returns:
#         List of restaurant recommendations
#     """
#     cuisine = cuisine_type if cuisine_type else "local traditional"
#
#     prompt = f"""Find restaurant recommendations in {destination}:
#
# Cuisine: {cuisine}
# Price Range: {price_range}
#
# Provide 5 restaurants with:
# 1. Name and type of cuisine
# 2. Why it's recommended
# 3. Typical price range for a meal
# 4. Must-try dishes
# """
#
#     result = call_llm(prompt)
#
#     return {
#         "destination": destination,
#         "cuisine": cuisine,
#         "price_range": price_range,
#         "recommendations": result
#     }

# ============================================================================
# TODO 2: ITINERARY BUILDER (agents/itinerary_builder.py)
# ============================================================================
# Create day-by-day travel itineraries.
#
# """
# Itinerary Builder - Create structured travel plans.
#
# ROLE:
# Take research data and create day-by-day itineraries
# with timing, locations, and practical tips.
#
# OUTPUT FORMAT:
# Day 1: [Theme]
#   - Morning: Activity
#   - Lunch: Restaurant
#   - Afternoon: Activity
#   - Evening: Activity/Dinner
# """
#
# from agents.base import call_llm
# from typing import Dict, List
#
# def build_itinerary(destination: str, days: int, dates: str = "",
#                     preferences: Dict = None) -> str:
#     """
#     Build a complete day-by-day itinerary.
#
#     Args:
#         destination: Place to visit
#         days: Number of days
#         dates: Specific dates
#         preferences: Dict with interests, pace, budget
#
#     Returns:
#         Formatted itinerary text
#     """
#     prefs = preferences or {}
#     interests = prefs.get("interests", "general sightseeing")
#     pace = prefs.get("pace", "moderate")  # relaxed/moderate/busy
#     budget = prefs.get("budget", "midrange")
#
#     prompt = f"""Create a {days}-day itinerary for {destination}.
#
# Dates: {dates if dates else "Flexible"}
# Interests: {interests}
# Pace: {pace} (relaxed = 2-3 activities/day, moderate = 3-4, busy = 5+)
# Budget: {budget}
#
# Format each day as:
#
# **Day 1: [Theme]**
# 🕐 Morning: [Time] - [Activity] ([Duration])
#    📍 Location: [Name/Address]
#    💡 Tip: [Practical tip]
# 🍽️ Lunch: [Recommendation] ([$])
# 🕐 Afternoon: [Time] - [Activity]
# ...
# 🌙 Evening: [Dinner/Activity]
#
# Include:
# - Travel time between locations
# - Meal breaks
# - Rest time
# - Realistic timing
# """
#
#     return call_llm(prompt)
#
# def add_day_trip(main_itinerary: str, day_trip_destination: str,
#                  day: int = None) -> str:
#     """
#     Add a day trip to existing itinerary.
#
#     Args:
#         main_itinerary: Existing itinerary text
#         day_trip_destination: Place for day trip
#         day: Which day to add it to (None = suggest best day)
#
#     Returns:
#         Updated itinerary
#     """
#     prompt = f"""Suggest where to add a day trip to {day_trip_destination}
# within this itinerary, or create a full day trip plan:
#
# Current Itinerary:
# {main_itinerary}
#
# Day Trip Destination: {day_trip_destination}
#
# Provide:
# 1. Which day works best (if not specified)
# 2. Full day trip plan with timing
# 3. Transportation details
# 4. What to see/do there
# """
#
#     return call_llm(prompt)
#
# def optimize_route(day_activities: List[Dict]) -> List[Dict]:
#     """
#     Optimize order of activities to minimize travel.
#
#     Args:
#         day_activities: List of activities with locations
#
#     Returns:
#         Reordered list with travel info
#     """
#     activities_str = "\n".join([
#         f"- {a['name']} at {a.get('location', 'TBD')}"
#         for a in day_activities
#     ])
#
#     prompt = f"""Optimize the order of these activities to minimize travel time:
#
# {activities_str}
#
# Consider:
# - Geographic clustering
# - Opening hours
# - Peak crowd times
#
# Return reordered list with:
# 1. Suggested order
# 2. Estimated travel time between stops
# 3. Total travel time for the day
# """
#
#     result = call_llm(prompt)
#
#     return {
#         "original": day_activities,
#         "optimized": result
#     }

# ============================================================================
# TODO 3: BUDGET CALCULATOR (agents/budget_calculator.py)
# ============================================================================
# Estimate and track trip costs.
#
# """
# Budget Calculator - Estimate trip costs and track spending.
#
# ROLE:
# Provide cost estimates for destinations,
# track planned expenses, identify budget risks.
#
# COST CATEGORIES:
# - Flights
# - Accommodation
# - Food
# - Activities
# - Transportation
# - Miscellaneous
# """
#
# from tinydb import TinyDB
# from datetime import datetime
# from typing import Dict, List
#
# class BudgetCalculator:
#     def __init__(self, db_path: str = "travel_budget.json"):
#         self.db = TinyDB(db_path)
#         self.trips = self.db.table("trips")
#
#     def create_budget(self, destination: str, days: int,
#                      budget_level: str = "midrange") -> Dict:
#         """
#         Create estimated budget for a trip.
#
#         Args:
#             destination: Travel destination
#             days: Trip length
#             budget_level: budget/midrange/luxury
#
#         Returns:
#             Dict with category estimates
#         """
#         multipliers = {
#             "budget": {"flights": 0.3, "accommodation": 0.2, "food": 0.2,
#                       "activities": 0.15, "transport": 0.1, "misc": 0.05},
#             "midrange": {"flights": 0.25, "accommodation": 0.25, "food": 0.2,
#                         "activities": 0.15, "transport": 0.1, "misc": 0.05},
#             "luxury": {"flights": 0.2, "accommodation": 0.35, "food": 0.2,
#                       "activities": 0.1, "transport": 0.1, "misc": 0.05}
#         }
#
#         daily_estimates = {
#             "budget": 75,
#             "midrange": 175,
#             "luxury": 400
#         }
#
#         daily = daily_estimates.get(budget_level, 175)
#         total = daily * days
#         ratios = multipliers.get(budget_level, multipliers["midrange"])
#
#         budget = {
#             "destination": destination,
#             "days": days,
#             "budget_level": budget_level,
#             "total_estimate": total,
#             "daily_breakdown": {
#                 category: total * ratio
#                 for category, ratio in ratios.items()
#             }
#         }
#
#         return budget
#
#     def save_trip(self, trip_data: Dict) -> int:
#         """Save a trip plan to database."""
#         trip_data["created"] = datetime.now().isoformat()
#         return self.trips.insert(trip_data)
#
#     def get_trip(self, trip_id: int) -> Dict:
#         """Get saved trip by ID."""
#         return self.trips.get(doc_id=trip_id)
#
#     def get_all_trips(self) -> List[Dict]:
#         """Get all saved trips."""
#         return self.trips.all()
#
# def estimate_flight_cost(origin: str, destination: str,
#                          cabin: str = "economy") -> Dict:
#     """
#     Estimate flight costs (placeholder - real app would use API).
#     """
#     prompt = f"""Estimate round-trip flight cost from {origin} to {destination}.
#
# Cabin: {cabin}
#
# Provide:
# 1. Estimated price range (low/high)
# 2. Typical airlines that fly this route
# 3. Flight duration
# 4. Best time to book for deals
# """
#
#     result = call_llm(prompt)
#
#     return {
#         "route": f"{origin} → {destination}",
#         "cabin": cabin,
#         "estimate": result
#     }

# ============================================================================
# TODO 4: BOOKING HELPER (agents/booking_helper.py)
# ============================================================================
# Format booking information and links.
#
# """
# Booking Helper - Format booking info for easy reference.
#
# ROLE:
# Take confirmed itinerary items and format them
# into easy-to-use booking references.
#
# OUTPUT:
# - Confirmation numbers
# - Addresses
# - Directions
# - What to have ready
# """
#
# from agents.base import call_llm
# from typing import Dict, List
#
# def format_flight_info(flight_details: Dict) -> str:
#     """
#     Format flight confirmation info.
#
#     Args:
#         flight_details: Dict with airline, times, confirmation
#
#     Returns:
#         Formatted flight info
#     """
#     prompt = f"""Format this flight into a clear confirmation:
#
# {flight_details}
#
# Include:
# 1. Airline and flight number
# 2. Date and time (departure and arrival)
# 3. Airports (code and name)
# 4. Terminal and gate (if known)
# 5. Confirmation/PNR number
# 6. Check-in deadline
# 7. What to have ready (ID, documents)
# """
#
#     return call_llm(prompt)
#
# def format_hotel_info(hotel_details: Dict) -> str:
#     """
#     Format hotel confirmation.
#     """
#     prompt = f"""Format this hotel booking:
#
# {hotel_details}
#
# Include:
# 1. Hotel name and star rating
# 2. Address with neighborhood
# 3. Check-in/out times
# 4. Confirmation number
# 5. Room type
# 6. Amenities included
# 7. Check-in instructions (late arrival? key pickup?)
# """
#
#     return call_llm(prompt)
#
# def create_day_summary(activities: List[Dict]) -> str:
#     """
#     Create a daily schedule summary for reference.
#
#     Args:
#         activities: List of planned activities
#
#     Returns:
#         Formatted day plan
#     """
#     activities_str = "\n".join([
#         f"- {a.get('time', 'TBD')}: {a.get('name', 'Activity')}"
#         for a in activities
#     ])
#
#     prompt = f"""Create a clean daily summary from this:
#
# {activities_str}
#
# Format as:
# 🗓️ [DAY, DATE]
#
# ⏰ [Time] - [Activity]
#    📍 [Location/Address]
#
# Keep it scannable for quick reference during the day.
# """
#
#     return call_llm(prompt)

# ============================================================================
# TODO 5: FRONTEND (frontend.py)
# ============================================================================
# import streamlit as st
# from agents.destination_researcher import research_destination
# from agents.itinerary_builder import build_itinerary
# from agents.budget_calculator import BudgetCalculator
# from agents.packing_list import generate_packing_list
#
# st.title("✈️ AI Travel Planner")
#
# # Trip planning form
# st.header("Plan Your Trip")
#
# col1, col2 = st.columns(2)
# with col1:
#     destination = st.text_input("Destination", placeholder="e.g., Tokyo, Japan")
#     dates = st.text_input("Travel Dates", placeholder="e.g., March 15-22, 2025")
# with col2:
#     days = st.number_input("Number of days", 1, 30, 5)
#     budget = st.select_slider("Budget", ["Budget", "Midrange", "Luxury"])
#
# interests = st.multiselect(
#     "Interests",
#     ["Sightseeing", "Food & Dining", "Art & Culture", "Nature",
#      "Adventure", "Shopping", "Nightlife", "History"],
#     default=["Sightseeing", "Food & Dining"]
# )
#
# if st.button("Research Destination"):
#     with st.spinner("Researching destination..."):
#         research = research_destination(destination, dates)
#         st.session_state["research"] = research
#
#     st.success("Research complete!")
#
# if "research" in st.session_state:
#     st.divider()
#     st.header("Destination Research")
#     st.write(st.session_state["research"])
#
#     st.divider()
#     st.header("Build Itinerary")
#
#     if st.button("Generate Itinerary"):
#         with st.spinner("Building your trip..."):
#             itinerary = build_itinerary(
#                 destination, days, dates,
#                 {"interests": ", ".join(interests), "budget": budget.lower()}
#             )
#             st.session_state["itinerary"] = itinerary
#
#         st.success("Itinerary ready!")
#
#     if "itinerary" in st.session_state:
#         st.text_area("Your Itinerary", st.session_state["itinerary"], height=400)
#
#         # Download option
#         st.download_button(
#             "Download Itinerary",
#             st.session_state["itinerary"],
#             file_name=f"{destination.replace(' ', '_')}_itinerary.txt"
#         )
#
#     # Budget estimate
#     st.divider()
#     st.header("Budget Estimate")
#
#     calc = BudgetCalculator()
#     budget_estimate = calc.create_budget(destination, days, budget.lower())
#
#     col1, col2, col3 = st.columns(3)
#     col1.metric("Total Estimate", f"${budget_estimate['total_estimate']}")
#     col2.metric("Daily Average", f"${budget_estimate['total_estimate']//days}")
#     col3.metric("Budget Level", budget)
#
#     st.write("Breakdown:")
#     for cat, amount in budget_estimate["daily_breakdown"].items():
#         st.write(f"  {cat.title()}: ${amount:.0f}")
#
#     # Packing list
#     st.divider()
#     st.header("Packing List")
#
#     if st.button("Generate Packing List"):
#         packing = generate_packing_list(destination, dates, interests)
#         st.text_area("Packing List", packing, height=300)