import streamlit as st
from utils.load_data import load_data

st.set_page_config(
    page_title="Connection Test",
    layout="wide"
)

st.title("RESOLVE Internship Analytics Portal")

students_df = load_data()

st.success("Google Sheet Connected Successfully!")

st.metric(
    "Total Students",
    len(students_df)
)
st.write(students_df.columns.tolist())

st.write("## Dataset Preview")

st.dataframe(
    students_df,
    use_container_width=True,
    hide_index=True
)