"""
Placement Analytics Page.
"""

import streamlit as st

from components.app import initialize_app

from utils.analytics import (
    get_placement_summary,
    get_project_summary,
    get_supervisor_summary,
)
from utils.load_data import load_data


def main() -> None:
    """
    Display placement, supervisor, and project allocation statistics.
    """

    initialize_app()

    st.title("📍 Placements")

    st.caption(
        "Placement, supervisor and project allocation statistics."
    )

    # ---------------------------------------------------------
    # Load Data
    # ---------------------------------------------------------

    df = load_data()

    # ---------------------------------------------------------
    # Analytics
    # ---------------------------------------------------------

    placement_summary = get_placement_summary(df)

    supervisor_summary = get_supervisor_summary(df)

    project_summary = get_project_summary(df)

    # ---------------------------------------------------------
    # KPIs
    # ---------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Placement Shifts",
            len(placement_summary),
        )

    with col2:
        st.metric(
            "Supervisors",
            len(supervisor_summary),
        )

    with col3:
        st.metric(
            "Projects",
            len(project_summary),
        )

    # ---------------------------------------------------------
    # Placement Distribution
    # ---------------------------------------------------------

    st.subheader("Placement Distribution")

    st.dataframe(
        placement_summary,
        width="stretch",
        hide_index=True,
    )

    # ---------------------------------------------------------
    # Supervisor Allocation
    # ---------------------------------------------------------

    st.subheader("Supervisor Allocation")

    st.dataframe(
        supervisor_summary,
        width="stretch",
        hide_index=True,
    )

    # ---------------------------------------------------------
    # Project Allocation
    # ---------------------------------------------------------

    st.subheader("Project Allocation")

    st.dataframe(
        project_summary,
        width="stretch",
        hide_index=True,
    )

    # ---------------------------------------------------------
    # Placement Details
    # ---------------------------------------------------------

    st.subheader("Placement Details")

    for shift in sorted(df["placement"].dropna().unique()):

        st.markdown(f"### {shift}")

        shift_df = df[
            df["placement"] == shift
        ]

        st.dataframe(
            shift_df[
                [
                    "serial_number",
                    "name",
                    "university",
                    "supervisor",
                    "project_assigned",
                    "remarks",
                ]
            ],
            width="stretch",
            hide_index=True,
        )


if __name__ == "__main__":
    main()