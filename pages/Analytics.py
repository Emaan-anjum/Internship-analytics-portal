"""
Analytics Dashboard.
"""

import streamlit as st

from components.app import initialize_app

from utils.load_data import load_data
from utils.charts import (
    create_cgpa_histogram,
    create_degree_distribution_chart,
    create_shift_distribution_chart,
    create_university_distribution_chart,
)


def main() -> None:
    """
    Display the Analytics dashboard.
    """

    initialize_app()

    st.title("📈 Analytics")

    df = load_data()

    st.plotly_chart(
        create_university_distribution_chart(df),
        width="stretch",
    )

    st.plotly_chart(
        create_degree_distribution_chart(df),
        width="stretch",
    )

    st.plotly_chart(
        create_cgpa_histogram(df),
        width="stretch",
    )

    st.plotly_chart(
        create_shift_distribution_chart(df),
        width="stretch",
    )


if __name__ == "__main__":
    main()