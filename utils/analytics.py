"""
Analytics functions for the RESOLVE Internship Analytics Portal.

This module contains reusable functions for calculating
key performance indicators (KPIs) and summary statistics
from the internship dataset.
"""

import pandas as pd


def _get_numeric_series(
    df: pd.DataFrame,
    column_name: str,
) -> pd.Series:
    """
    Convert a DataFrame column to a numeric pandas Series.

    Parameters
    ----------
    df : pandas.DataFrame
        Internship dataset.

    column_name : str
        Name of the numeric column.

    Returns
    -------
    pandas.Series
        Numeric values with invalid entries converted to NaN.
    """

    if column_name not in df.columns:
        raise KeyError(
            f"Column '{column_name}' not found in the dataset."
        )

    return pd.to_numeric(
        df[column_name],
        errors="coerce",
    )


def get_total_students(df: pd.DataFrame) -> int:
    """
    Return the total number of students.
    """

    return len(df)


def get_total_universities(df: pd.DataFrame) -> int:
    """
    Return the total number of unique universities.
    """

    return df["university"].dropna().nunique()


def get_total_supervisors(df: pd.DataFrame) -> int:
    """
    Return the total number of unique supervisors.
    """

    return df["supervisor"].dropna().nunique()


def get_average_cgpa(df: pd.DataFrame) -> float:
    """
    Return the average CGPA.
    """

    cgpa = _get_numeric_series(df, "cgpa")

    return round(cgpa.mean(), 2)


def get_min_cgpa(df: pd.DataFrame) -> float:
    """
    Return the minimum CGPA.
    """

    cgpa = _get_numeric_series(df, "cgpa")

    return round(cgpa.min(), 2)


def get_max_cgpa(df: pd.DataFrame) -> float:
    """
    Return the maximum CGPA.
    """

    cgpa = _get_numeric_series(df, "cgpa")

    return round(cgpa.max(), 2)


def get_morning_placements(df: pd.DataFrame) -> int:
    """
    Return the total number of RESOLVE (M) placements.
    """

    return (
        df["placement"]
        .fillna("")
        .str.strip()
        .str.upper()
        .eq("RESOLVE (M)")
        .sum()
    )


def get_evening_placements(df: pd.DataFrame) -> int:
    """
    Return the total number of RESOLVE (E) placements.
    """

    return (
        df["placement"]
        .fillna("")
        .str.strip()
        .str.upper()
        .eq("RESOLVE (E)")
        .sum()
    )