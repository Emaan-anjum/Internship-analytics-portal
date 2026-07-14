"""
Reusable section component for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st


def display_section(
    title: str,
    subtitle: str | None = None,
) -> None:
    """
    Display a dashboard section heading.

    Parameters
    ----------
    title : str
        Section title.

    subtitle : str, optional
        Short description shown below the title.
    """

    st.markdown(f"## {title}")

    if subtitle:
        st.caption(subtitle)

    st.divider()