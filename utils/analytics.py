"""
Analytics functions for the RESOLVE Internship Analytics Portal.

This module contains reusable functions that calculate KPIs
and aggregated statistics from the internship dataset.
"""

# -------------------------------------------------------------------
# Third-Party Imports
# -------------------------------------------------------------------

import pandas as pd


# -------------------------------------------------------------------
# KPI FUNCTIONS
# -------------------------------------------------------------------

def get_total_students(df: pd.DataFrame) -> int:
    """Return the total number of students."""
    return len(df)


def get_total_universities(df: pd.DataFrame) -> int:
    """Return the number of unique universities."""
    if "university" not in df.columns:
        return 0

    return df["university"].dropna().nunique()


def get_total_domains(df: pd.DataFrame) -> int:
    """Return the number of unique domains."""
    if "domain" not in df.columns:
        return 0

    return df["domain"].dropna().nunique()


def get_total_supervisors(df: pd.DataFrame) -> int:
    """Return the number of unique supervisors."""
    if "supervisor" not in df.columns:
        return 0

    return df["supervisor"].dropna().nunique()


# -------------------------------------------------------------------
# CGPA ANALYTICS
# -------------------------------------------------------------------

def get_average_cgpa(df: pd.DataFrame):

    if "cgpa" not in df.columns:
        return None

    cgpa = pd.to_numeric(df["cgpa"], errors="coerce")

    return round(cgpa.mean(), 2)


def get_min_cgpa(df: pd.DataFrame):

    if "cgpa" not in df.columns:
        return None

    cgpa = pd.to_numeric(df["cgpa"], errors="coerce")

    return round(cgpa.min(), 2)


def get_max_cgpa(df: pd.DataFrame):

    if "cgpa" not in df.columns:
        return None

    cgpa = pd.to_numeric(df["cgpa"], errors="coerce")

    return round(cgpa.max(), 2)


# -------------------------------------------------------------------
# DISTRIBUTIONS
# -------------------------------------------------------------------

def get_university_distribution(df: pd.DataFrame):

    if "university" not in df.columns:
        return pd.Series(dtype=int)

    return (
        df["university"]
        .value_counts()
        .sort_values(ascending=False)
    )


def get_domain_distribution(df: pd.DataFrame):

    if "domain" not in df.columns:
        return pd.Series(dtype=int)

    return (
        df["domain"]
        .value_counts()
        .sort_values(ascending=False)
    )


def get_supervisor_distribution(df: pd.DataFrame):

    if "supervisor" not in df.columns:
        return pd.Series(dtype=int)

    return (
        df["supervisor"]
        .value_counts()
        .sort_values(ascending=False)
    )


def get_placement_distribution(df: pd.DataFrame):

    if "placement" not in df.columns:
        return pd.Series(dtype=int)

    return (
        df["placement"]
        .value_counts()
        .sort_values(ascending=False)
    )