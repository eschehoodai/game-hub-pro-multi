import streamlit as st
import os

st.title("⚙️ Settings")

current_url = st.session_state.get('DOC_URL', 'Keine URL gesetzt')
st.text_input("Pokee.ai GCS-URL", value=current_url, key="new_url")

if st.button("💾 Speichern & Refresh"):
    st.session_state.DOC_URL = st.session_state.new_url
    st.success("URL gespeichert!")
    st.cache_data.clear()
    st.rerun()

if st.button("🗑️ Cache leeren"):
    st.cache_data.clear()
    st.success("Cache geleert!")
