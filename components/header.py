"""
Reusable header component for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st

from config import APP_NAME


def display_header() -> None:
    """
    Display the application header.
    """

    st.title(APP_NAME)

    st.caption(
        "Research Solutions & Ventures (SUPARCO)"
    )

    st.write(
        "Summer Internship Program 2026"
    )

    st.divider()