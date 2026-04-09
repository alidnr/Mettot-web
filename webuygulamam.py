import streamlit as st
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# --- ARKA PLAN FOTOĞRAFI ---
FOTOGRAF_ADI = "image_9.png.jpeg"

def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

img_base64 = get_base64(FOTOGRAF_ADI)

# --- TASARIM (CSS) ---
st.markdown(f"""
    <style>
    /* Gereksiz her şeyi kaldır */
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
    }}

    /* Arka plan karartması */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.25);
        z-index: 0;
    }}

    /* ANA KONTEYNER - EKRANIN TAM ORTASINA SABİTLEME */
    .main-container {{
        position: fixed; /* Akıştan bağımsız, ekrana sabit */
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%); /* Tam matematiksel merkez */
        width: 100%;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }}

    .mettot-header {{
        color: white;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-shadow: 2px 2px 15px rgba(0,0,0,1);
        margin-bottom: 25px;
    }}

    .my-button {{
        background-color: rgba(0, 0, 0, 0.5);
        color: white !important;
        border: 1.5px solid white;
        border-radius: 10px;
        text-decoration: none !important;
        font-weight: bold;
        transition: 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto;
    }}

    /* BİLGİSAYAR AYARI */
    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 75px; }}
        .my-button {{ font-size: 22px; padding: 15px 45px; width: 320px; }}
    }}

    /* MOBİL AYARI - TAM ORTALANMIŞ GÖRÜNTÜ */
    @media (max-width: 768px) {{
        .mettot-header {{ 
            font-size: 42px; 
            margin-bottom: 20px;
        }}
        .my-button {{ 
            font-size: 18px; 
            padding: 14px 0; 
            width: 80%; 
        }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://spotify.com" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
