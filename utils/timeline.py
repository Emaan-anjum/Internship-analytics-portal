"""
Timeline analytics utilities.
"""

from datetime import datetime, timedelta

import pandas as pd

from config import INTERNSHIP_DURATION_WEEKS


def prepare_timeline(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add internship timeline columns.
    """

    timeline_df = df.copy()

    timeline_df["joining_date"] = pd.to_datetime(
        timeline_df["joining_date"],
        errors="coerce",
    )

    timeline_df["internship_end_date"] = (
        timeline_df["joining_date"]
        + timedelta(weeks=INTERNSHIP_DURATION_WEEKS)
    )

    today = pd.Timestamp.today().normalize()

    timeline_df["days_remaining"] = (
        timeline_df["internship_end_date"] - today
    ).dt.days

    timeline_df["status"] = timeline_df["days_remaining"].apply(
        lambda x: "Completed" if pd.notna(x) and x < 0 else "Active"
    )

    return timeline_df


def timeline_summary(df: pd.DataFrame) -> dict:
    """
    Calculate dashboard timeline KPIs.
    """

    timeline_df = prepare_timeline(df)

    today = pd.Timestamp.today().normalize()

    end_dates = timeline_df["internship_end_date"]

    active = (end_dates >= today).sum()

    ending_this_week = (
        (end_dates >= today)
        & (end_dates <= today + timedelta(days=7))
    ).sum()

    ending_next_week = (
        (end_dates > today + timedelta(days=7))
        & (end_dates <= today + timedelta(days=14))
    ).sum()

    return {
        "active": int(active),
        "ending_this_week": int(ending_this_week),
        "ending_next_week": int(ending_next_week),
        "earliest_completion": end_dates.min(),
        "latest_completion": end_dates.max(),
    }