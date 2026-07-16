"""
Chart utilities for the RESOLVE Internship Analytics Portal.
"""

import plotly.express as px
import pandas as pd

from config import (
    PRIMARY_BLUE,
    PRIMARY_ORANGE,
)


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

    fig.update_layout(
        title="Students by University",
        template="plotly_white",
        height=300,
        coloraxis_showscale=False,
    )

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

    fig.update_layout(
        title="Degree Distribution",
        template="plotly_white",
        height=300,
    )

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

    fig.update_layout(
        title="CGPA Distribution",
        template="plotly_white",
        height=300,
    )

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

    fig.update_layout(
        title="Placement Shift Distribution",
        template="plotly_white",
        height=300,
        showlegend=False,
    )

    return fig