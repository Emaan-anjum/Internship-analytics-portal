"""
Main entry point for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st

from config import (
    APP_ICON,
    APP_NAME,
)

from utils.load_data import load_data

from components.theme import apply_theme
from components.header import display_header
from components.dashboard_kpis import display_dashboard_kpis


def configure_page() -> None:
    """
    Configure the Streamlit page.
    """

    st.set_page_config(
        page_title=APP_NAME,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )


def main() -> None:
    """
    Launch the dashboard.
    """

    configure_page()

    apply_theme() 

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