import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

# DEINE DRIVE-DATEI-ID (aus dem Link zwischen /d/ und /view)
FILE_ID = "1V4yzrLHz2-STOIjphTfB2SraTvll5RPU"

# DIREKTER DOWNLOAD-LINK (funktioniert für öffentliche Dateien)
DIRECT_URL = f"https://drive.google.com/uc?export=download&id={FILE_ID}"

@st.cache_data(ttl=1800)
def fetch_games():
    try:
        r = requests.get(DIRECT_URL, headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        
        games = []
        for row in soup.find('table').find_all('tr')[1:]:  # Skip header
            cols = row.find_all('td')
            if len(cols) >= 4:
                games.append({
                    'name': cols[0].get_text(strip=True),
                    'release': cols[1].get_text(strip=True),
                    'genre': cols[2].find('span').get_text(strip=True) if cols[2].find('span') else cols[2].get_text(strip=True),
                    'desc': cols[3].get_text(strip=True)
                })
        return games
    except Exception as e:
        st.error(f"Drive-Fehler: {e}")
        return []
