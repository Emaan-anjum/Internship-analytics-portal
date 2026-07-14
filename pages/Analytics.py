"""
Analytics Dashboard.
"""

import streamlit as st

from utils.load_data import load_data
from utils.charts import (
    create_cgpa_histogram,
    create_degree_distribution_chart,
    create_shift_distribution_chart,
    create_university_distribution_chart,
)

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