import streamlit as st

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# RESMİN DOĞRUDAN LİNKİ (Hızlı yükleme için)
RESIM_URL = "https://i.ibb.co/Fkqwf5xF/image-9-png.jpg"

# --- TASARIM (CSS) ---
st.markdown(f"""
    <style>
    /* Streamlit bileşenlerini tamamen gizle */
    header, footer, .stDeployButton {{display: none !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    /* Arka plan ayarı - En hızlı yöntem */
    .stApp {{
        background: linear-gradient(rgba(0,0,0,0.3), rgba(0,0,0,0.3)), 
                    url("{RESIM_URL}") center center / cover no-repeat fixed;
        height: 100vh;
        width: 100vw;
    }}

    /* Ana konteyner - Tam orta */
    .main-container {{
        position: fixed;
        top: 50%;
        left: 50%;
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
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-shadow: 2px 2px 15px rgba(0,0,0,1);
        margin-bottom: 30px;
    }}

    /* Profesyonel Cam (Glassmorphism) Butonlar */
    .my-button {{
        background-color: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(8px);
        -webkit-backdrop-filter: blur(8px);
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 12px;
        text-decoration: none !important;
        font-weight: bold;
        transition: 0.3s all ease;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 12px auto;
    }}

    /* Hover (Üzerine gelince parlatma ve büyütme) */
    .my-button:hover {{
        background-color: rgba(255, 255, 255, 0.25);
        border: 1px solid white;
        transform: scale(1.05);
        box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.2);
    }}

    /* Masaüstü ayarı */
    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 80px; }}
        .my-button {{ font-size: 22px; padding: 18px 0; width: 340px; }}
    }}

    /* Mobil ayarı */
    @media (max-width: 768px) {{
        .mettot-header {{ font-size: 48px; }}
        .my-button {{ font-size: 18px; padding: 15px 0; width: 85%; }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com/artist/6xi4UQoVjPLTld9Fu12736?si=xne1GWFqQQeQaEJV5alviQ" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
