import streamlit as st
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# --- ARKA PLAN FOTOĞRAFI FONKSİYONU ---
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
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        height: 100vh;
        width: 100vw;
        overflow: hidden;
    }}

    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 0;
    }}

    .main-container {{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        width: 100%;
        z-index: 10;
    }}

    .mettot-header {{
        color: white;
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-shadow: 2px 2px 15px rgba(0,0,0,1);
        margin-bottom: 20px;
    }}

    .my-button {{
        background-color: rgba(255, 255, 255, 0.1);
        color: white !important;
        border: 2px solid white;
        border-radius: 10px;
        text-decoration: none !important;
        font-weight: bold;
        transition: 0.3s;
        backdrop-filter: blur(5px);
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 10px auto;
    }}

    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 80px; }}
        .my-button {{ font-size: 22px; padding: 15px 40px; width: 250px; }}
    }}

    @media (max-width: 768px) {{
        .mettot-header {{ font-size: 45px; }}
        .my-button {{ font-size: 18px; padding: 12px 0; width: 75%; }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
