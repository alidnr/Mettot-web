import streamlit as st
import base64

# Sayfa ayarlarını en başta yap
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# Fotoğrafı yükleyen fonksiyon (Hızlı cacheleme için optimize edildi)
@st.cache_data
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        return base64.b64encode(f.read()).decode()

# --- ARKA PLAN FOTOĞRAFI ---
# ÖNEMLİ: image_9.png.jpeg dosyasını sıkıştırıp WebP yaparsan çok daha hızlı olur!
try:
    img_base64 = get_base64("image_9.png.jpeg")
except:
    img_base64 = ""

# --- TASARIM ---
st.markdown(f"""
    <style>
    /* CSS render hızını artırmak için sadeleştirildi */
    header, footer, .stDeployButton {{display: none !important;}}
    .block-container {{padding: 0px !important;}}
    
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.25), rgba(0,0,0,0.25)), 
                    url("data:image/jpeg;base64,{img_base64}") center center / cover no-repeat fixed;
        height: 100vh;
        width: 100vw;
    }}

    .main-container {{
        position: fixed;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        z-index: 10;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }}

    .mettot-header {{
        color: white;
        font-family: 'Courier New', monospace;
        font-size: 42px;
        font-weight: bold;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.8);
        margin-bottom: 20px;
    }}

    .my-button {{
        background-color: rgba(0, 0, 0, 0.5);
        color: white !important;
        border: 1px solid white;
        border-radius: 10px;
        text-decoration: none !important;
        font-weight: bold;
        padding: 14px 0;
        width: 80%;
        max-width: 320px;
        margin: 8px auto;
        display: block;
        transition: transform 0.2s, background 0.2s;
    }}

    /* Hover (Üzerine gelince parlama) efekti ekledik - Profesyonel dokunuş */
    .my-button:hover {{
        background-color: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);
    }}

    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 75px; }}
        .my-button {{ width: 300px; padding: 15px 0; }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com/artist/6xi4UQoVjPLTld9Fu12736?si=xne1GWFqQQeQaEJV5alviQ" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
