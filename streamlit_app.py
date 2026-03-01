import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout="wide")
st.title("AI Equity Research Dashboard")

@st.cache_data
def load_data():
return pd.read_parquet("factors.parquet")

df = load_data()

latest_date = df["date"].max()
df_today = df[df["date"] == latest_date]

st.subheader("Composite Score Distribution")

fig = px.histogram(df_today, x="composite_score", nbins=20)
st.plotly_chart(fig, use_container_width=True)

st.subheader("Top 20 Long Candidates")

longs = df_today.sort_values("composite_score", ascending=False).head(20)
st.dataframe(longs[["symbol", "composite_score"]])
