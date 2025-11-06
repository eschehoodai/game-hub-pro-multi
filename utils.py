import streamlit as st
import requests
from bs4 import BeautifulSoup
import re
import os

@st.cache_data(ttl=1800)
def fetch_games(_force=False):
    url = st.session_state.get('DOC_URL', os.getenv('DOC_URL', "https://storage.googleapis.com/pokee-api-bucket/user_350nB0KCk3rbjsg6f3VE8EMa63v/021c9724-294c-4c28-9de4-938f11c8ae8b/html_report.html?X-Goog-Algorithm=GOOG4-RSA-SHA256&X-Goog-Credential=pokee-storage-access%40verdant-option-419105.iam.gserviceaccount.com%2F20251104%2Fauto%2Fstorage%2Fgoog4_request&X-Goog-Date=20251104T230505Z&X-Goog-Expires=604799&X-Goog-SignedHeaders=host&X-Goog-Signature=67951e345bfcf3f96ce6d56502a969e467b255ff08c4205b3b596b98047a33c2a107b23d2780a264d8215c50e2e4a70eb740a96be303829be010375badf161d46c425157a118a686e58eca1806c6992012e09c34b9cd9c370a3651ff8521d118a83b01d1e0965e7785037d59e44e1dceae8048bb22e3e806bce9f705e63b457ec0a327f902d8903a9c38cfcd39355f796d52b34a0c199c7bec5d4230b92653491dbc89653b39901818b9cde279ae078b531730e850190ecc65aab8a13b5d485c0aa7af835c06fac34a3cd44a15241d707b841540ee3c391514095b807af6296cd70beea2531c864f0cb2b91acf2800589a075b3965f87bef90131650de256a95"))
    
    try:
        r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        r.raise_for_status()
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'html.parser')
        games = []
        seen = set()
        
        for block in soup.find_all('div', class_='game-section'):
            h2 = block.find('h2')
            title = h2.get_text(strip=True) if h2 else None
            ps = [p for p in block.find_all('p') if p.get_text(strip=True)]
            combined = " ".join(p.get_text() for p in ps)
            
            name = re.search(r'Name:\s*(.+)', combined, re.IGNORECASE)
            release = re.search(r'Erscheinungsdatum:\s*(.+)', combined, re.IGNORECASE)
            genre = re.search(r'Genre:\s*(.+)', combined, re.IGNORECASE)
            desc = re.search(r'Zusammenfassung:\s*([\s\S]+?)(?=Quelle:|$)', combined, re.IGNORECASE)
            quelle = re.search(r'Quelle:\s*(.+)', combined, re.IGNORECASE)
            
            name_val = name.group(1).strip() if name else title
            if not name_val or name_val in seen:
                continue
            seen.add(name_val)
            
            games.append({
                'name': name_val,
                'release': release.group(1).strip() if release else 'TBD',
                'genre': genre.group(1).strip() if genre else 'Unknown',
                'desc': desc.group(1).strip()[:300] + '...' if desc else 'No desc.',
                'quelle': quelle.group(1).strip() if quelle else 'Unknown'
            })
        return games
    except:
        return []
