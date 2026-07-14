"""
Universities Analytics Page.
"""

import streamlit as st

from utils.load_data import load_data


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

summary = (
    df.groupby("university")
    .agg(
        Students=("serial_number", "count"),
        Average_CGPA=("cgpa", "mean"),
        Minimum_CGPA=("cgpa", "min"),
        Maximum_CGPA=("cgpa", "max"),
    )
    .reset_index()
)

summary["Average_CGPA"] = summary["Average_CGPA"].round(2)
summary["Minimum_CGPA"] = summary["Minimum_CGPA"].round(2)
summary["Maximum_CGPA"] = summary["Maximum_CGPA"].round(2)

# ---------------------------------------------------------
# KPIs
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Universities",
        summary.shape[0],
    )

with col2:
    st.metric(
        "Total Students",
        len(df),
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

chart_data = summary.sort_values(
    by="Students",
    ascending=False,
)

st.bar_chart(
    chart_data.set_index("university")["Students"],
    width="stretch",
)