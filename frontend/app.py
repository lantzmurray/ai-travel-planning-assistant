import streamlit as st
import sys
import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_ROOT = os.path.dirname(os.path.dirname(PROJECT_ROOT))
sys.path.insert(0, PROJECT_ROOT)
if PACKAGE_ROOT not in sys.path:
    sys.path.insert(0, PACKAGE_ROOT)

from agents.base import get_session_history
from orchestrator import Orchestrator
from components import render_app_footer, run_with_status_updates

st.set_page_config(page_title="Travel Planning Assistant", layout="wide")


def render_session_log(session_id: str) -> None:
    """Display the stored collaboration log for this travel-planning run."""
    history = get_session_history(session_id)
    if not history:
        return

    st.subheader("Planning Log")
    for entry in history:
        timestamp = entry["timestamp"].replace("T", " ")
        with st.expander(f"{entry['agent']} · {timestamp}", expanded=False):
            st.markdown(entry["content"])


def main():
    st.title("Travel Planning Assistant")
    st.caption("Help users collaboratively plan trips with AI agents.")

    st.sidebar.title("Trip Inputs")
    destination = st.sidebar.text_input(
        "Destination",
        placeholder="Tokyo, Japan",
    )
    travel_dates = st.sidebar.text_input(
        "Travel Dates",
        placeholder="Late November for a 5-day trip",
    )
    budget = st.sidebar.text_input(
        "Budget",
        placeholder="Midrange budget for a 4-day trip",
    )
    interests = st.text_area(
        "Interests",
        height=180,
        placeholder="Food markets, architecture, quiet cafes, and easy day trips.",
    )

    if st.button("Run Planning Team", type="primary"):
        if not destination.strip():
            st.warning("Add a destination so the planning agents have a clear target.")
            return

        inputs = {
            "destination": destination.strip(),
            "travel_dates": travel_dates.strip(),
            "budget": budget.strip(),
            "interests": interests.strip(),
        }
        orch = Orchestrator()
        output = run_with_status_updates(
            lambda: orch.run_workflow(inputs),
            start_message="Agents are building the travel plan..."
        )

        st.success(f"Workflow Complete! Session ID: {output['session_id']}")

        for agent, response in output["results"].items():
            with st.expander(f"{agent} Response", expanded=True):
                st.markdown(response)

        render_session_log(output["session_id"])


    render_app_footer()

if __name__ == "__main__":
    main()
