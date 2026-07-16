"""
Internship Timeline Page
------------------------
Displays internship progress, completion schedule,
and remaining duration for all interns.
"""

import streamlit as st

from components.app import initialize_app
from components.header import display_header

from utils.load_data import load_data
from utils.timeline import (
    prepare_timeline,
    timeline_summary,
)


# ==========================================================
# Initialize Application
# ==========================================================

initialize_app()

# ==========================================================
# Page Title
# ==========================================================

st.subheader("📅 Internship Timeline")

st.caption(
    "Monitor internship progress, completion dates, and remaining duration."
)

st.divider()

# ==========================================================
# Load Data
# ==========================================================

df = load_data()

timeline_df = prepare_timeline(df)

summary = timeline_summary(df)

# ==========================================================
# Timeline Overview
# ==========================================================

st.markdown("### 📊 Timeline Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👨‍💼 Active Interns",
        summary["active"],
    )

with col2:
    st.metric(
        "⏳ Ending This Week",
        summary["ending_this_week"],
    )

with col3:
    st.metric(
        "📅 Ending Next Week",
        summary["ending_next_week"],
    )

st.divider()

# ==========================================================
# Completion Window
# ==========================================================

st.markdown("### 🗓 Internship Completion Window")

left, right = st.columns(2)

with left:
    st.metric(
        "Earliest Completion",
        summary["earliest_completion"].strftime("%d %b %Y"),
    )

with right:
    st.metric(
        "Latest Completion",
        summary["latest_completion"].strftime("%d %b %Y"),
    )

st.divider()

# ==========================================================
# Timeline Table
# ==========================================================

st.markdown("### 📋 Internship Timeline")

display_columns = [
    "serial_number",
    "name",
    "university",
    "placement",
    "joining_date",
    "internship_end_date",
    "days_remaining",
    "status",
]

timeline_table = (
    timeline_df[display_columns]
    .sort_values("internship_end_date")
    .copy()
)

timeline_table["joining_date"] = (
    timeline_table["joining_date"]
    .dt.strftime("%d %b %Y")
)

timeline_table["internship_end_date"] = (
    timeline_table["internship_end_date"]
    .dt.strftime("%d %b %Y")
)

st.dataframe(
    timeline_table,
    use_container_width=True,
    hide_index=True,
)