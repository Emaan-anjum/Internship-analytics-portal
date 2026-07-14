"""
Dashboard KPI section for the RESOLVE Internship Analytics Portal.
"""

import pandas as pd
import streamlit as st

from utils.analytics import (
    get_average_cgpa,
    get_evening_placements,
    get_max_cgpa,
    get_min_cgpa,
    get_morning_placements,
    get_total_students,
    get_total_supervisors,
    get_total_universities,
)


def display_dashboard_kpis(df: pd.DataFrame) -> None:
    """
    Display dashboard KPI metrics.
    """

    st.subheader("📊 Dashboard Overview")

    kpis = [
        ("Total Students", get_total_students(df)),
        ("Universities", get_total_universities(df)),
        ("Supervisors", get_total_supervisors(df)),
        ("Average CGPA", f"{get_average_cgpa(df):.2f}"),
        ("Minimum CGPA", f"{get_min_cgpa(df):.2f}"),
        ("Maximum CGPA", f"{get_max_cgpa(df):.2f}"),
        ("Morning Placements", get_morning_placements(df)),
        ("Evening Placements", get_evening_placements(df)),
    ]

    cards_per_row = 4

    for i in range(0, len(kpis), cards_per_row):

        cols = st.columns(cards_per_row)

        for col, (title, value) in zip(cols, kpis[i:i + cards_per_row]):

            with col:

                st.metric(
                    label=title,
                    value=value,
                )