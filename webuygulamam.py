import streamlit as st
import base64
import os

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# --- ARKA PLAN FOTOĞRAFI ---
FOTOGRAF_ADI = "image_9.png.jpeg"

def get_base64_of_bin_file(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except FileNotFoundError:
        return None

bin_str = get_base64_of_bin_file(FOTOGRAF_ADI)

# --- TASARIM VE KESİN MERKEZLEME (CSS) ---
st.markdown(f"""
    <style>
    /* Gereksiz Streamlit parçalarını tamamen temizle */
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str if bin_str else ""}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}

    /* Karartma Katmanı */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 0;
    }}

    /* ANA KONTEYNER: Her şeyi tam merkeze zorla */
    .main-container {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        width: 100%;
        z-index: 10;
    }}

    /* DEV METTOT BAŞLIĞI */
    .mettot-header {{
        color: white;
        font-size: 110px; /* Daha da büyüttük */
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        margin-bottom: 40px;
        text-shadow: 5px 5px 20px rgba(0,0,0,1);
    }}

    /* BUTONLAR */
    .button-group {{
        display: flex;
        justify-content: center;
        gap: 25px;
    }}

    .my-button {{
        background-color: rgba(0,0,0,0.7);
        color: white !important;
        padding: 20px 45px;
        border: 3px solid white;
        border-radius: 15px;
        text-decoration: none !important;
        font-size: 28px;
        font-weight: bold;
        transition: 0.3s;
    }}

    .my-button:hover {{
        background-color: white;
        color: black !important;
        transform: scale(1.1);
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">&lt; METTOT &gt;</div>
        <div class="button-group">
            <a href="https://open.spotify.com/artist/6xi4UQoVjPLTld9Fu12736?si=Eds9g7BTSzeBVXvfFPjlZA" target="_blank" class="my-button">Spotify</a>
            <a href="https://www.instagram.com/enessjordan?igsh=ZWZsdjNrOWxxNTNt" target="_blank" class="my-button">Instagram</a>
            <a href="https://youtube.com/@mettot-sx?si=Tp6uCZLPhxA6ewSd" target="_blank" class="my-button">YouTube</a>
        </div>
    </div>
""", unsafe_allow_html=True)