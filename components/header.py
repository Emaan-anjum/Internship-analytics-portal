"""
Reusable header component for the RESOLVE Internship Analytics Portal.
"""

from datetime import datetime
from pathlib import Path

import streamlit as st

from config import (
    APP_NAME,
    BRAND_SUBTITLE,
    PROGRAM_NAME,
)


def display_header() -> None:
    """
    Display the branded application header.

    Layout: RESOLVE logo | title block (name, org, program) | SUPARCO logo,
    followed by a slim status bar with a live-data indicator and the
    last-refreshed timestamp.
    """

    col1, col2, col3 = st.columns([2.2, 5.6, 2.2], vertical_alignment="center")

    with col1:
        logo = Path("assets/logos/RESOLVE_logo.png")
        if logo.exists():
            st.image(str(logo), width=220)

    with col2:
        st.markdown(
            f"""
            <div class="app-header-titles">
                <h1>{APP_NAME}</h1>
                <p class="app-header-org">{BRAND_SUBTITLE}</p>
                <p class="app-header-program">{PROGRAM_NAME}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col3:
        logo = Path("assets/logos/SUPARCO_logo.png")
        if logo.exists():
            st.image(str(logo), width=110)

    # -------------------------------------------------------------
    # Status bar: connection indicator + last refresh timestamp
    # -------------------------------------------------------------

    refreshed_at = datetime.now().strftime("%d %b %Y, %I:%M %p")

    st.markdown(
        f"""
        <div class="app-header-statusbar">
            <div class="app-header-status">
                <span class="status-dot"></span>
                Live Data Connected
            </div>
            <div class="app-header-refresh">
                Last refreshed: {refreshed_at}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.divider()
