"""
Degree Analytics Page.
"""

import streamlit as st

from components.app import initialize_app

from utils.analytics import (
    get_degree_summary,
    get_total_students,
)
from utils.load_data import load_data


def main() -> None:
    """
    Display degree-wise internship statistics.
    """

    initialize_app()

    st.title("🎓 Degrees")

    st.caption(
        "Degree-wise internship statistics."
    )

    # ---------------------------------------------------------
    # Load Data
    # ---------------------------------------------------------

    df = load_data()

    # ---------------------------------------------------------
    # Degree Summary
    # ---------------------------------------------------------

    summary = get_degree_summary(df)

    # ---------------------------------------------------------
    # KPIs
    # ---------------------------------------------------------

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Degrees",
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
    # Degree Statistics
    # ---------------------------------------------------------

    st.subheader("Degree Statistics")

    st.dataframe(
        summary,
        width="stretch",
        hide_index=True,
    )

    # ---------------------------------------------------------
    # Degree Distribution
    # ---------------------------------------------------------

    st.subheader("Students by Degree")

    st.bar_chart(
        summary
        .sort_values(
            by="Students",
            ascending=False,
        )
        .set_index("degree")["Students"],
        width="stretch",
    )

    # ---------------------------------------------------------
    # Download Summary
    # ---------------------------------------------------------

    csv = summary.to_csv(
        index=False,
    ).encode("utf-8")

    st.download_button(
        label="📥 Download Degree Summary",
        data=csv,
        file_name="degree_summary.csv",
        mime="text/csv",
    )


if __name__ == "__main__":
    main()