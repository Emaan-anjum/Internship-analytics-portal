"""
Chart utilities for the RESOLVE Internship Analytics Portal.
"""

import plotly.express as px
import pandas as pd

from config import (
    CHART_HEIGHT,
    GRID_COLOR,
    PRIMARY_BLUE,
    PRIMARY_ORANGE,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
)


def _apply_resolve_chart_style(fig, title: str):
    """
    Apply the shared RESOLVE visual style to a Plotly figure.

    This only touches layout/presentation (fonts, margins, grid,
    hover, legend, title styling) — it never modifies the
    underlying data, trace values, or calculations.
    """

    fig.update_layout(
        title={
            "text": f"<b>{title}</b>",
            "x": 0.02,
            "xanchor": "left",
            "font": {"size": 17, "color": TEXT_PRIMARY, "family": "Inter, sans-serif"},
        },
        template="plotly_white",
        height=CHART_HEIGHT,
        font=dict(family="Inter, sans-serif", size=13, color=TEXT_SECONDARY),
        margin=dict(l=40, r=30, t=60, b=40),
        hoverlabel=dict(
            bgcolor="white",
            bordercolor=PRIMARY_BLUE,
            font=dict(family="Inter, sans-serif", size=13, color=TEXT_PRIMARY),
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(size=12),
        ),
        plot_bgcolor="white",
        paper_bgcolor="rgba(0,0,0,0)",
    )

    fig.update_xaxes(showgrid=False, linecolor=GRID_COLOR, title_font=dict(size=13))
    fig.update_yaxes(showgrid=True, gridcolor=GRID_COLOR, title_font=dict(size=13))

    return fig


def create_university_distribution_chart(
    df: pd.DataFrame,
):
    """
    Bar chart showing the number of students per university.
    """

    data = (
        df["university"]
        .value_counts()
        .reset_index()
    )

    data.columns = [
        "University",
        "Students",
    ]

    fig = px.bar(
        data,
        x="University",
        y="Students",
        color="Students",
        color_continuous_scale=[
            PRIMARY_BLUE,
            PRIMARY_ORANGE,
        ],
    )

    fig.update_layout(coloraxis_showscale=False)

    _apply_resolve_chart_style(fig, "Students by University")

    return fig


def create_degree_distribution_chart(
    df: pd.DataFrame,
):
    """
    Pie chart showing student degree distribution.
    """

    data = (
        df["degree"]
        .value_counts()
        .reset_index()
    )

    data.columns = [
        "Degree",
        "Students",
    ]

    fig = px.pie(
        data,
        names="Degree",
        values="Students",
        hole=0.45,
        color_discrete_sequence=[
            PRIMARY_BLUE,
            PRIMARY_ORANGE,
            "#4CAF50",
            "#9C27B0",
            "#03A9F4",
            "#FFC107",
        ],
    )

    _apply_resolve_chart_style(fig, "Degree Distribution")

    return fig


def create_cgpa_histogram(
    df: pd.DataFrame,
):
    """
    Histogram of student CGPAs.
    """

    fig = px.histogram(
        df,
        x="cgpa",
        nbins=10,
        color_discrete_sequence=[
            PRIMARY_BLUE,
        ],
    )

    _apply_resolve_chart_style(fig, "CGPA Distribution")

    return fig


def create_shift_distribution_chart(
    df: pd.DataFrame,
):
    """
    Morning vs Evening internship placements.
    """

    data = (
        df["placement"]
        .value_counts()
        .reset_index()
    )

    data.columns = [
        "Shift",
        "Students",
    ]

    fig = px.bar(
        data,
        x="Shift",
        y="Students",
        color="Shift",
        color_discrete_sequence=[
            PRIMARY_BLUE,
            PRIMARY_ORANGE,
        ],
    )

    fig.update_layout(showlegend=False)

    _apply_resolve_chart_style(fig, "Placement Shift Distribution")

    return fig
