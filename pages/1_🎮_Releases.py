import streamlit as st
from utils import fetch_games

st.title("🎮 Neue PC Releases")
games = fetch_games()

if games:
    for g in games[:30]:
        with st.expander(f"**{g['name']}** • {g['release']} • {g['genre']}"):
            st.write(g['desc'])
            st.caption(f"🔗 [Quelle]({g['quelle']})")
else:
    st.error("Keine Games – prüfe Settings!")
