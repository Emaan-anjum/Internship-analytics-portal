"""
Reusable statistic card component for the RESOLVE Internship Analytics Portal.
"""

import streamlit as st


def display_stat_card(
    icon: str,
    title: str,
    value,
) -> None:
    """
    Display a statistic card.

    Parameters
    ----------
    icon : str
        Material icon or emoji.

    title : str
        Card title.

    value : Any
        Card value.
    """

    with st.container(border=True):

        st.markdown(
            f"""
            <div class="resolve-stat-icon">
                {icon}
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.metric(
            label=title,
            value=value,
        )