"""
Exports Page.
"""

import io

import pandas as pd
import streamlit as st

from components.app import initialize_app
from utils.load_data import load_data


def main() -> None:
    """
    Display export options for the internship dataset.
    """

    initialize_app()

    st.title("📤 Exports")

    st.caption(
        "Export internship data for reporting and further analysis."
    )

    # ---------------------------------------------------------
    # Load Data
    # ---------------------------------------------------------

    df = load_data()

    # ---------------------------------------------------------
    # Preview
    # ---------------------------------------------------------

    st.subheader("Dataset Preview")

    st.dataframe(
        df,
        width="stretch",
        hide_index=True,
    )

    # ---------------------------------------------------------
    # CSV Export
    # ---------------------------------------------------------

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="resolve_internship_data.csv",
        mime="text/csv",
    )

    # ---------------------------------------------------------
    # Excel Export
    # ---------------------------------------------------------

    excel_buffer = io.BytesIO()

    with pd.ExcelWriter(
        excel_buffer,
        engine="openpyxl",
    ) as writer:

        df.to_excel(
            writer,
            index=False,
            sheet_name="Internship Data",
        )

    excel_buffer.seek(0)

    st.download_button(
        label="⬇️ Download Excel",
        data=excel_buffer,
        file_name="resolve_internship_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )


if __name__ == "__main__":
    main()