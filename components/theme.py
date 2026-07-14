"""
Theme configuration for the RESOLVE Internship Analytics Portal.

This module applies the global visual theme.
"""

import streamlit as st

from config import (
    BORDER_COLOR,
    BORDER_RADIUS,
    PAGE_BACKGROUND,
    PRIMARY_BLUE,
    PRIMARY_ORANGE,
    SIDEBAR_BACKGROUND,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)


def apply_theme() -> None:
    """
    Apply the RESOLVE Design System.
    """

    st.markdown(
        f"""
<style>

/* ==========================================================
   Typography
========================================================== */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: "Inter", sans-serif;
}}

/* ==========================================================
   App
========================================================== */

.stApp {{
    background-color: {PAGE_BACKGROUND};
    color: {TEXT_PRIMARY};
}}

.block-container {{
    max-width: 1400px;
    padding: 2rem;
}}

/* ==========================================================
   Global Text
========================================================== */

.stApp,
.stApp div,
.stApp span,
.stApp p,
.stApp label,
.stMarkdown,
[data-testid="stMarkdownContainer"] {{
    color: {TEXT_PRIMARY} !important;
}}

p {{
    color: {TEXT_SECONDARY} !important;
}}

/* ==========================================================
   Headings
========================================================== */

h1,
h2,
h3,
h4 {{
    color: {PRIMARY_BLUE} !important;
    font-weight: 700;
}}

/* ==========================================================
   Sidebar
========================================================== */

section[data-testid="stSidebar"] {{
    background-color: {SIDEBAR_BACKGROUND};
    border-right: 3px solid {PRIMARY_ORANGE};
}}

section[data-testid="stSidebar"] * {{
    color: {TEXT_PRIMARY} !important;
}}

/* ==========================================================
   Buttons
========================================================== */

.stButton > button {{
    background-color: {PRIMARY_BLUE};
    color: white;
    border: none;
    border-radius: 8px;
    font-weight: 600;
}}

.stButton > button:hover {{
    background-color: {PRIMARY_ORANGE};
}}

/* ==========================================================
   Metrics
========================================================== */

div[data-testid="stMetric"] {{
    border: 1px solid {BORDER_COLOR};
    border-radius: {BORDER_RADIUS};
    padding: 0.75rem;
}}

div[data-testid="stMetricLabel"] label {{
    color: {TEXT_SECONDARY} !important;
}}

div[data-testid="stMetricValue"] {{
    color: {PRIMARY_BLUE} !important;
    font-weight: 700;
}}

/* ==========================================================
   DataFrame
========================================================== */

div[data-testid="stDataFrame"] {{
    border: 1px solid {BORDER_COLOR};
    border-radius: {BORDER_RADIUS};
    overflow: hidden;
}}

/* ==========================================================
   Divider
========================================================== */

hr {{
    border: none;
    border-top: 2px solid {PRIMARY_ORANGE};
}}

/* ==========================================================
   Scrollbar
========================================================== */

::-webkit-scrollbar {{
    width: 10px;
}}

::-webkit-scrollbar-thumb {{
    background: {PRIMARY_BLUE};
    border-radius: 20px;
}}

::-webkit-scrollbar-thumb:hover {{
    background: {PRIMARY_ORANGE};
}}

</style>
""",
        unsafe_allow_html=True,
    )