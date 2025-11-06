import streamlit as st
from utils import fetch_games
import pandas as pd

st.title("📊 Stats & Trends")
games = fetch_games()
df = pd.DataFrame(games)

col1, col2 = st.columns(2)
with col1:
    st.metric("Total Games", len(df))
with col2:
    st.metric("Genres", df['genre'].nunique())

st.bar_chart(df['genre'].value_counts().head(10))
