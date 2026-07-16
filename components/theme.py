"""
Theme loader for the RESOLVE Internship Analytics Portal.

Loads the global CSS stylesheet and injects branding assets.
"""

from pathlib import Path

import streamlit as st


def apply_theme() -> None:
    """
    Load the global RESOLVE stylesheet.
    """

    css_path = Path("assets/css/theme.css")

    if css_path.exists():
        st.markdown(
            f"<style>{css_path.read_text(encoding='utf-8')}</style>",
            unsafe_allow_html=True,
        )