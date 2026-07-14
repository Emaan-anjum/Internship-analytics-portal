"""
Reusable card component for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st


def open_card() -> None:
    """
    Open a RESOLVE styled card.
    """

    st.markdown(
        """
        <div class="resolve-card">
        """,
        unsafe_allow_html=True,
    )


def close_card() -> None:
    """
    Close a RESOLVE styled card.
    """

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True,
    )