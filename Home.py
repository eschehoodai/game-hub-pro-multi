import streamlit as st

st.set_page_config(page_title="Game Hub Pro", page_icon="🎮", layout="wide")

st.title("🎮 Game Hub Pro – Multi-Page Edition")
st.markdown("**Deine tägliche PC-Game-Release-Maschine** – powered by Pokee.ai + Grok 3")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("https://img.icons8.com/fluency/96/000000/controller.png")
with col2:
    st.metric("Seiten", 5)
with col3:
    st.metric("Quellen", "Pokee.ai GCS")

st.markdown("### 🚀 Wähle eine Seite links aus!")
st.markdown("""
- **Releases** → Alle neuen PC-Games  
- **News** → Frische MMORPG-News  
- **Settings** → URL ändern & Cache  
- **Stats** → Charts & Trends  
- **About** → Dein Portfolio  
""")
