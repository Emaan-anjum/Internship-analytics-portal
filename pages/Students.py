"""
Students Page for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st

from utils.load_data import load_data


st.title("👨‍🎓 Students")

st.caption(
    "Browse, search and filter internship records."
)

# ---------------------------------------------------------
# Load Data
# ---------------------------------------------------------

df = load_data()

# ---------------------------------------------------------
# Filters
# ---------------------------------------------------------

st.subheader("Filters")

col1, col2, col3 = st.columns(3)

with col1:

    selected_university = st.selectbox(
        "University",
        ["All"] + sorted(df["university"].dropna().unique().tolist())
    )

with col2:

    selected_degree = st.selectbox(
        "Degree",
        ["All"] + sorted(df["degree"].dropna().unique().tolist())
    )

with col3:

    selected_placement = st.selectbox(
        "Placement",
        ["All"] + sorted(df["placement"].dropna().unique().tolist())
    )

# ---------------------------------------------------------
# Search
# ---------------------------------------------------------

search_text = st.text_input(
    "🔍 Search Student",
    placeholder="Enter student name..."
)

# ---------------------------------------------------------
# Apply Filters
# ---------------------------------------------------------

filtered_df = df.copy()

if selected_university != "All":
    filtered_df = filtered_df[
        filtered_df["university"] == selected_university
    ]

if selected_degree != "All":
    filtered_df = filtered_df[
        filtered_df["degree"] == selected_degree
    ]

if selected_placement != "All":
    filtered_df = filtered_df[
        filtered_df["placement"] == selected_placement
    ]

if search_text:

    filtered_df = filtered_df[
        filtered_df["name"]
        .astype(str)
        .str.contains(
            search_text,
            case=False,
            na=False,
        )
    ]

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

st.metric(
    "Students Found",
    len(filtered_df),
)

# ---------------------------------------------------------
# Display Table
# ---------------------------------------------------------

st.subheader("Student Records")

st.dataframe(
    filtered_df,
    width="stretch",
    hide_index=True,
)

# ---------------------------------------------------------
# Export
# ---------------------------------------------------------

csv = filtered_df.to_csv(
    index=False,
).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Data",
    data=csv,
    file_name="students.csv",
    mime="text/csv",
)