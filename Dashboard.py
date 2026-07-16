"""
Main entry point for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st

from utils.load_data import load_data

from components.app import initialize_app
from components.header import display_header
from components.dashboard_kpis import display_dashboard_kpis


def main() -> None:
    """
    Launch the dashboard.
    """

    initialize_app()

    students_df = load_data()

    # ---------------------------------------------------------
    # Dashboard Header
    # ---------------------------------------------------------

    display_header()

    # ---------------------------------------------------------
    # KPI Overview
    # ---------------------------------------------------------

    display_dashboard_kpis(students_df)

    st.markdown("")

    # ---------------------------------------------------------
    # Student Records
    # ---------------------------------------------------------

    st.subheader("📋 Student Records")

    st.dataframe(
        students_df,
        use_container_width=True,
        hide_index=True,
    )


if __name__ == "__main__":
    main()