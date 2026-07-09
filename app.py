import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Internship Analytics Portal")

df = pd.DataFrame({
    "University": ["GIKI", "UET", "FAST"],
    "Students": [18, 26, 15]
})

fig = px.bar(df, x="University", y="Students")

st.plotly_chart(fig)