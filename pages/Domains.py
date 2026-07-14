"""
Degree Analytics Page.
"""

import streamlit as st

from utils.load_data import load_data


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

summary = (
    df.groupby("degree")
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
        "Degrees",
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

chart_data = summary.sort_values(
    by="Students",
    ascending=False,
)

st.bar_chart(
    chart_data.set_index("degree")["Students"],
    width="stretch",
)

# ---------------------------------------------------------
# Download Summary
# ---------------------------------------------------------

csv = summary.to_csv(
    index=False,
).encode("utf-8")

st.download_button(
    "📥 Download Degree Summary",
    data=csv,
    file_name="degree_summary.csv",
    mime="text/csv",
)