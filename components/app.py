"""
Application bootstrap for the RESOLVE Internship Analytics Portal.

This module performs all common application initialization
required by every page.
"""

import streamlit as st
from components.theme import apply_theme
from components.sidebar import render_sidebar

from config import (
    APP_ICON,
    APP_NAME,
)


# =========================================================
# Page Configuration
# =========================================================

def configure_page() -> None:
    """
    Configure the Streamlit application.
    """

    st.set_page_config(
        page_title=APP_NAME,
        page_icon=APP_ICON,
        layout="wide",
        initial_sidebar_state="expanded",
    )


# =========================================================
# Session State
# =========================================================

def initialize_session() -> None:
    """
    Initialize global session variables.
    """

    defaults = {
        "theme_loaded": True,
        "animations_enabled": True,
    }

    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


# =========================================================
# Application Bootstrap
# =========================================================

def initialize_app() -> None:

    configure_page()

    apply_theme()

    render_sidebar()

    initialize_session()
