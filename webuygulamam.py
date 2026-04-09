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
    /* Streamlit öğelerini gizle */
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        width: 100vw;
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    /* Karartma katmanı */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.4);
        z-index: 0;
    }}

    /* ANA KONTEYNER */
    .main-container {{
        z-index: 10;
        width: 100%;
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }}

    .mettot-header {{
        color: white;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(0,0,0,1);
        text-align: center;
        margin-bottom: 25px;
    }}

    .my-button {{
        background-color: rgba(0, 0, 0, 0.6); /* Butonları biraz daha belirgin yaptık */
        color: white !important;
        border: 1px solid rgba(255,255,255,0.5);
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: bold;
        text-align: center;
        transition: 0.3s;
        display: block;
        margin: 8px 0;
    }}

    /* BİLGİSAYAR AYARI */
    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 70px; }}
        .my-button {{ font-size: 20px; padding: 15px 40px; width: 300px; }}
    }}

    /* MOBİL AYARI - Her şeyi aşağı kaydırdık ve küçülttük */
    @media (max-width: 768px) {{
        .main-container {{
            margin-top: -100px; /* İçeriği biraz yukarı veya aşağı almak için burayı değiştirebilirsin */
        }}
        .mettot-header {{ font-size: 40px; }}
        .my-button {{ 
            font-size: 16px; 
            padding: 14px 0; 
            width: 85%; /* Butonlar ekrana daha iyi yayılır */
        }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
