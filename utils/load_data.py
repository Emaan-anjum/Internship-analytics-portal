import re

import gspread
import pandas as pd
import streamlit as st
from google.oauth2.service_account import Credentials

from config import (
    CREDENTIALS_PATH,
    SPREADSHEET_NAME,
)


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]


def clean_column_name(column_name: str) -> str:
    """
    Convert column names into Python-friendly format.

    Example
    -------
    PHONE NUMBER -> phone_number
    JOINING DATE -> joining_date
    CGPA -> cgpa
    """

    column_name = column_name.strip().lower()

    column_name = re.sub(r"[^\w\s]", "", column_name)

    column_name = re.sub(r"\s+", "_", column_name)

    return column_name


@st.cache_data(show_spinner=False)
def load_data() -> pd.DataFrame:
    """
    Read internship data from Google Sheets.

    Returns
    -------
    pandas.DataFrame
        Clean internship dataset.
    """

    credentials = Credentials.from_service_account_file(
        CREDENTIALS_PATH,
        scopes=SCOPES,
    )

    client = gspread.authorize(credentials)

    spreadsheet = client.open(SPREADSHEET_NAME)

    worksheet = spreadsheet.sheet1

    all_data = worksheet.get_all_values()

    # --------------------------------------------------------
    # Sheet Layout
    #
    # Row 4 : Category Headers
    # Row 5 : Actual Headers
    # Row 6 : Student Records
    # --------------------------------------------------------

    category_row = all_data[3]
    header_row = all_data[4]

    # --------------------------------------------------------
    # Fill merged category cells
    # --------------------------------------------------------

    categories = []

    current_category = ""

    for value in category_row:

        if value.strip():

            current_category = value.strip()

        categories.append(current_category)

    final_headers = []

    for category, header in zip(categories, header_row):

        category = category.strip()

        header = header.strip()

        if header:

            final_headers.append(header)

        else:

            final_headers.append(category)

    # --------------------------------------------------------
    # Extract Student Records Only
    # --------------------------------------------------------

    student_rows = []

    for row in all_data[5:]:

        # Skip completely empty rows

        if not any(cell.strip() for cell in row):

            continue

        # Stop before Spare Projects section

        row_text = " ".join(row).lower()

        if "spare" in row_text and "project" in row_text:

            break

        student_rows.append(row)

    students_df = pd.DataFrame(
        student_rows,
        columns=final_headers,
    )

    # --------------------------------------------------------
    # Standardize Column Names
    # --------------------------------------------------------

    columns = students_df.columns.tolist()

    # Rename first column

    columns[0] = "serial_number"

    students_df.columns = [
        clean_column_name(column)
        for column in columns
    ]

    # --------------------------------------------------------
    # Replace Empty Strings
    # --------------------------------------------------------

    students_df.replace("", pd.NA, inplace=True)

    # --------------------------------------------------------
    # Remove Empty Rows
    # --------------------------------------------------------

    students_df.dropna(
        how="all",
        inplace=True,
    )

    # --------------------------------------------------------
    # Trim Whitespace
    # --------------------------------------------------------

    for column in students_df.select_dtypes(include="object"):

        students_df[column] = (
            students_df[column]
            .astype(str)
            .str.strip()
            .replace("nan", pd.NA)
        )

    # --------------------------------------------------------
    # Remove Invalid Student Records
    # --------------------------------------------------------

    if "name" in students_df.columns:

        students_df = students_df[
            students_df["name"].notna()
        ]

        students_df = students_df[
            students_df["name"] != ""
        ]

    # --------------------------------------------------------
    # Convert Numeric Columns
    # --------------------------------------------------------

    numeric_columns = [
        "serial_number",
        "cgpa",
        "semester",
    ]

    for column in numeric_columns:

        if column in students_df.columns:

            students_df[column] = pd.to_numeric(
                students_df[column],
                errors="coerce",
            )

    # --------------------------------------------------------
    # Convert Date Columns
    # --------------------------------------------------------

    date_columns = [
        "joining_date",
    ]

    for column in date_columns:

        if column in students_df.columns:

            students_df[column] = pd.to_datetime(
                students_df[column],
                errors="coerce",
            )

    # --------------------------------------------------------
    # Reset Index
    # --------------------------------------------------------

    students_df.reset_index(
        drop=True,
        inplace=True,
    )

    return students_df