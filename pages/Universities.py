"""
Universities Analytics Page.
"""

import streamlit as st

from components.app import initialize_app

from utils.analytics import (
    get_total_students,
    get_university_summary,
)
from utils.load_data import load_data


def main() -> None:
    """
    Display university-wise internship statistics.
    """

    initialize_app()

    st.title("🏫 Universities")

    st.caption(
        "University-wise internship statistics."
    )

    # ---------------------------------------------------------
    # Load Data
    # ---------------------------------------------------------

    df = load_data()

    # ---------------------------------------------------------
    # University Summary
    # ---------------------------------------------------------

    summary = get_university_summary(df)

    # ---------------------------------------------------------
    # KPIs
    # ---------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Universities",
            len(summary),
        )

    with col2:
        st.metric(
            "Total Students",
            get_total_students(df),
        )

    with col3:
        st.metric(
            "Highest Average CGPA",
            f"{summary['Average_CGPA'].max():.2f}",
        )

    # ---------------------------------------------------------
    # University Statistics
    # ---------------------------------------------------------

    st.subheader("University Statistics")

    st.dataframe(
        summary,
        width="stretch",
        hide_index=True,
    )

    # ---------------------------------------------------------
    # Top Universities
    # ---------------------------------------------------------

    st.subheader("Top Universities by Student Count")

    st.bar_chart(
        summary
        .sort_values(
            by="Students",
            ascending=False,
        )
        .set_index("university")["Students"],
        width="stretch",
    )


if __name__ == "__main__":
    main()