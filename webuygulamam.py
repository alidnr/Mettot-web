import streamlit as st
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# Fotoğrafı hızlıca yüklemek için cache kullanıyoruz
@st.cache_data
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

# --- DOSYA ADI ---
# GitHub'da yaptığın yeni isim:
FOTOGRAF_ADI = "arka_plan.webp" 
img_base64 = get_base64(FOTOGRAF_ADI)

# --- TASARIM (CSS) ---
st.markdown(f"""
    <style>
    /* Gereksiz öğeleri gizle */
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.45), rgba(0, 0, 0, 0.45)),
                    url("data:image/webp;base64,{img_base64}") center center / cover no-repeat fixed;
        height: 100vh;
        width: 100vw;
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .main-container {{
        position: fixed;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        z-index: 10;
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }}

    .mettot-header {{
        color: white;
        font-family: 'Courier New', monospace;
        font-weight: bold;
        text-shadow: 2px 2px 20px rgba(0,0,0,1);
        margin-bottom: 30px;
        letter-spacing: 5px;
    }}

    .my-button {{
        background-color: rgba(255, 255, 255, 0.1);
        color: white !important;
        border: 1.5px solid rgba(255, 255, 255, 0.4);
        border-radius: 15px;
        text-decoration: none !important;
        font-weight: bold;
        transition: 0.4s ease;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 12px auto;
        backdrop-filter: blur(8px); /* Cam efekti */
    }}

    /* Üzerine gelince (Hover) Efekti */
    .my-button:hover {{
        background-color: rgba(255, 255, 255, 0.25);
        border-color: white;
        transform: scale(1.05); /* Hafif büyüme */
        box-shadow: 0px 0px 25px rgba(255, 255, 255, 0.3);
    }}

    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 85px; }}
        .my-button {{ font-size: 22px; padding: 18px 0; width: 350px; }}
    }}

    @media (max-width: 768px) {{
        .mettot-header {{ font-size: 48px; }}
        .my-button {{ font-size: 20px; padding: 16px 0; width: 85%; }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com/user/317v2hsvtq663pbeogbpg25ha" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
