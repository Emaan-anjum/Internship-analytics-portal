"""
Sidebar component for the RESOLVE Internship Analytics Portal.

The sidebar is intentionally kept minimal because the page
navigation is managed by Streamlit's multipage system.
"""

import streamlit as st


def render_sidebar() -> None:
    """
    Render a clean sidebar.

    Streamlit automatically renders the page navigation.
    This function only adds minimal styling information.
    """

    st.sidebar.markdown(
        """
        <div style="height:12px;"></div>
        """,
        unsafe_allow_html=True,
    )