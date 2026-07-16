"""
Reusable header component for the RESOLVE Internship Analytics Portal.
"""

from pathlib import Path

import streamlit as st

from config import APP_NAME


"""
Reusable header component for the RESOLVE Internship Analytics Portal.
"""

from pathlib import Path
import streamlit as st

from config import APP_NAME


"""
Reusable header component for the RESOLVE Internship Analytics Portal.
"""

from pathlib import Path
import streamlit as st

from config import APP_NAME


def display_header() -> None:
    """
    Display the branded application header.
    """

    col1, col2, col3 = st.columns([2.2, 5.6, 2.2], vertical_alignment="center")

    with col1:
        logo = Path("assets/logos/RESOLVE_logo.png")
        if logo.exists():
            st.image(str(logo), width=500)

    with col2:
        st.markdown(
            f"<h1 style='text-align:center; color:#111827; margin-bottom:0;'>{APP_NAME}</h1>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align:center; color:#5B6B82; font-size:22px; margin-bottom:0;'>Research Solutions & Ventures (SUPARCO)</p>",
            unsafe_allow_html=True,
        )

        st.markdown(
            "<p style='text-align:center; color:#94A3B8; font-size:18px;'>Summer Internship Program 2026</p>",
            unsafe_allow_html=True,
        )

    with col3:
        logo = Path("assets/logos/SUPARCO_logo.png")
        if logo.exists():
            st.image(str(logo), width=120)

    st.divider()