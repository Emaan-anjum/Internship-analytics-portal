"""
Placement Analytics Page.
"""

import streamlit as st

from utils.load_data import load_data


st.title("📍 Placements")

st.caption(
    "Placement, supervisor and project allocation statistics."
)

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

df = load_data()

# ---------------------------------------------------------
# KPIs
# ---------------------------------------------------------

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Placement Shifts",
        df["placement"].nunique(),
    )

with col2:

    st.metric(
        "Supervisors",
        df["supervisor"].nunique(),
    )

with col3:

    st.metric(
        "Projects",
        df["project_assigned"].nunique(),
    )

# ---------------------------------------------------------
# Placement Distribution
# ---------------------------------------------------------

st.subheader("Placement Distribution")

placement_summary = (
    df.groupby("placement")
    .size()
    .reset_index(name="Students")
)

st.dataframe(
    placement_summary,
    width="stretch",
    hide_index=True,
)

st.bar_chart(
    placement_summary.set_index("placement")["Students"],
    width="stretch",
)

# ---------------------------------------------------------
# Supervisor Allocation
# ---------------------------------------------------------

st.subheader("Supervisor Allocation")

supervisor_summary = (
    df.groupby("supervisor")
    .size()
    .reset_index(name="Students")
    .sort_values(
        "Students",
        ascending=False,
    )
)

st.dataframe(
    supervisor_summary,
    width="stretch",
    hide_index=True,
)

# ---------------------------------------------------------
# Project Allocation
# ---------------------------------------------------------

st.subheader("Project Allocation")

project_summary = (
    df.groupby("project_assigned")
    .size()
    .reset_index(name="Students")
    .sort_values(
        "Students",
        ascending=False,
    )
)

st.dataframe(
    project_summary,
    width="stretch",
    hide_index=True,
)

# ---------------------------------------------------------
# Placement Details by Shift
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