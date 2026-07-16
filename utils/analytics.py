"""
Business analytics module for the RESOLVE Internship Analytics Portal.

This module serves as the Business Intelligence Layer of the application.
It contains reusable analytical functions that calculate key performance
indicators (KPIs), summary statistics, and business metrics from the
internship dataset.

Responsibilities
----------------
• Dashboard KPIs
• University Analytics
• Degree Analytics
• Placement Analytics
• Timeline Analytics (future)
• Data Quality Analytics (future)

This module intentionally contains NO Streamlit code.
"""

from __future__ import annotations

import pandas as pd

# ==========================================================
# Internal Helper Functions
# ==========================================================

def _get_numeric_series(
    df: pd.DataFrame,
    column_name: str,
) -> pd.Series:
    """
    Return a DataFrame column converted to numeric values.
    Invalid entries are converted to NaN.
    """

    if column_name not in df.columns:
        raise KeyError(
            f"Column '{column_name}' not found."
        )

    return pd.to_numeric(
        df[column_name],
        errors="coerce",
    )


def _create_summary_table(
    df: pd.DataFrame,
    group_column: str,
) -> pd.DataFrame:
    """
    Create a reusable CGPA summary table.

    Returns
    -------
    DataFrame

    Columns:
        group_column
        Students
        Average_CGPA
        Minimum_CGPA
        Maximum_CGPA
    """

    summary = (
        df.groupby(group_column)
        .agg(
            Students=("serial_number", "count"),
            Average_CGPA=("cgpa", "mean"),
            Minimum_CGPA=("cgpa", "min"),
            Maximum_CGPA=("cgpa", "max"),
        )
        .reset_index()
    )

    summary["Average_CGPA"] = (
        summary["Average_CGPA"]
        .round(2)
    )

    summary["Minimum_CGPA"] = (
        summary["Minimum_CGPA"]
        .round(2)
    )

    summary["Maximum_CGPA"] = (
        summary["Maximum_CGPA"]
        .round(2)
    )

    return summary


def _create_count_summary(
    df: pd.DataFrame,
    column_name: str,
    value_name: str = "Students",
) -> pd.DataFrame:
    """
    Create a frequency summary table.

    Parameters
    ----------
    column_name
        Column to summarize.

    value_name
        Name of the count column.
    """

    return (
        df.groupby(column_name)
        .size()
        .reset_index(name=value_name)
        .sort_values(
            by=value_name,
            ascending=False,
        )
    )

# ==========================================================
# Dashboard KPIs
# ==========================================================

def get_total_students(
    df: pd.DataFrame,
) -> int:
    """
    Return the total number of internship students.
    """

    return len(df)


def get_total_universities(
    df: pd.DataFrame,
) -> int:
    """
    Return the total number of participating universities.
    """

    return (
        df["university"]
        .dropna()
        .nunique()
    )


def get_total_supervisors(
    df: pd.DataFrame,
) -> int:
    """
    Return the total number of supervisors.
    """

    return (
        df["supervisor"]
        .dropna()
        .nunique()
    )


def get_average_cgpa(
    df: pd.DataFrame,
) -> float:
    """
    Return the average CGPA.
    """

    cgpa = _get_numeric_series(
        df,
        "cgpa",
    )

    return round(
        cgpa.mean(),
        2,
    )


def get_min_cgpa(
    df: pd.DataFrame,
) -> float:
    """
    Return the minimum CGPA.
    """

    cgpa = _get_numeric_series(
        df,
        "cgpa",
    )

    return round(
        cgpa.min(),
        2,
    )


def get_max_cgpa(
    df: pd.DataFrame,
) -> float:
    """
    Return the maximum CGPA.
    """

    cgpa = _get_numeric_series(
        df,
        "cgpa",
    )

    return round(
        cgpa.max(),
        2,
    )


def get_morning_placements(
    df: pd.DataFrame,
) -> int:
    """
    Return the number of RESOLVE (M) interns.
    """

    return (
        df["placement"]
        .fillna("")
        .str.strip()
        .str.upper()
        .eq("RESOLVE (M)")
        .sum()
    )


def get_evening_placements(
    df: pd.DataFrame,
) -> int:
    """
    Return the number of RESOLVE (E) interns.
    """

    return (
        df["placement"]
        .fillna("")
        .str.strip()
        .str.upper()
        .eq("RESOLVE (E)")
        .sum()
    )


def get_dashboard_summary(
    df: pd.DataFrame,
) -> dict[str, float]:
    """
    Return all dashboard KPIs in a single dictionary.

    This function acts as the primary entry point for the
    dashboard page, allowing all KPI values to be retrieved
    with a single function call.
    """

    return {
        "total_students": get_total_students(df),
        "total_universities": get_total_universities(df),
        "total_supervisors": get_total_supervisors(df),
        "average_cgpa": get_average_cgpa(df),
        "minimum_cgpa": get_min_cgpa(df),
        "maximum_cgpa": get_max_cgpa(df),
        "morning_placements": get_morning_placements(df),
        "evening_placements": get_evening_placements(df),
    }
# ==========================================================
# University Analytics
# ==========================================================

def get_university_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return university-wise internship statistics.

    Columns
    -------
    university
    Students
    Average_CGPA
    Minimum_CGPA
    Maximum_CGPA
    """

    return _create_summary_table(
        df,
        "university",
    )

# ==========================================================
# Degree Analytics
# ==========================================================

def get_degree_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return degree-wise internship statistics.

    Columns
    -------
    degree
    Students
    Average_CGPA
    Minimum_CGPA
    Maximum_CGPA
    """

    return _create_summary_table(
        df,
        "degree",
    )

# ==========================================================
# Placement Analytics
# ==========================================================

def get_placement_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return placement-wise student distribution.
    """

    return _create_count_summary(
        df,
        "placement",
    )


def get_supervisor_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return supervisor workload summary.
    """

    return _create_count_summary(
        df,
        "supervisor",
    )


def get_project_summary(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Return project allocation summary.
    """

    return _create_count_summary(
        df,
        "project_assigned",
    )

# ==========================================================
# Timeline Analytics
# ==========================================================

# Reserved for Version 2.0


# ==========================================================
# Data Quality Analytics
# ==========================================================

# Reserved for Version 2.0