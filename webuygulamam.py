import streamlit as st
import base64

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Mettot-Sx", layout="wide")

@st.cache_data
def get_base64(bin_file):
    try:
        with open(bin_file, 'rb') as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return None

# --- DOSYA ADI ---
# GitHub'daki ismin tam hali: resim_9.png.jpeg.webp
FOTOGRAF_ADI = "resim_9.png.jpeg.webp" 
img_base64 = get_base64(FOTOGRAF_ADI)

# --- TASARIM ---
if img_base64:
    bg_style = f"""
    <style>
    .stApp {{
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
                    url("data:image/webp;base64,{img_base64}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    </style>
    """
else:
    # Fotoğraf yüklenemezse siyah arka plan yap
    bg_style = """<style>.stApp { background-color: #0e1117; }</style>"""

st.markdown(bg_style, unsafe_allow_html=True)

st.markdown(f"""
    <style>
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    .stApp {{
        height: 100vh;
        width: 100vw;
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
        text-shadow: 2px 2px 15px rgba(0,0,0,1);
        margin-bottom: 25px;
    }}

    .my-button {{
        background-color: rgba(255, 255, 255, 0.1);
        color: white !important;
        border: 1.5px solid rgba(255, 255, 255, 0.5);
        border-radius: 12px;
        text-decoration: none !important;
        font-weight: bold;
        transition: 0.3s ease-in-out;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 12px auto;
        backdrop-filter: blur(5px);
    }}

    .my-button:hover {{
        background-color: rgba(255, 255, 255, 0.2);
        border-color: white;
        transform: scale(1.05);
        box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.3);
    }}

    @media (min-width: 769px) {{
        .mettot-header {{ font-size: 80px; }}
        .my-button {{ font-size: 22px; padding: 16px 0; width: 340px; }}
    }}

    @media (max-width: 768px) {{
        .mettot-header {{ font-size: 45px; }}
        .my-button {{ font-size: 19px; padding: 15px 0; width: 85%; }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com/artist/6xi4UQoVjPLTld9Fu12736?si=xne1GWFqQQeQaEJV5alviQ" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
