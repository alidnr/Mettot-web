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

# --- TASARIM VE KESİN MERKEZLEME (CSS) ---
st.markdown(f"""
    <style>
    /* Streamlit öğelerini gizle */
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    .block-container {{padding: 0px !important; margin: 0px !important;}}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center center;
        background-repeat: no-repeat;
        height: 100vh;
        width: 100vw;
        overflow: hidden; /* Kaydırmayı engelle */
    }}

    /* Karartma Katmanı */
    .stApp::before {{
        content: "";
        position: absolute;
        top: 0; left: 0; width: 100%; height: 100%;
        background-color: rgba(0, 0, 0, 0.2); /* Fotoğrafı çok kapatmamak için azaltıldı */
        z-index: 0;
    }}

    /* ANA KONTEYNER */
    .main-container {{
        position: absolute;
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
        text-shadow: 2px 2px 10px rgba(0,0,0,1);
    }}

    .my-button {{
        background-color: rgba(0, 0, 0, 0.45); /* Şeffaflığı artırdık, fotoğraf engellemesin diye */
        color: white !important;
        border: 1.5px solid rgba(255,255,255,0.8); /* Kenarlığı daha ince ve şık yaptık */
        border-radius: 8px; /* Daha az yuvarlak, daha köşeli ve profesyonel */
        text-decoration: none !important;
        font-weight: bold;
        transition: 0.3s;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 8px auto;
    }}

    /* BİLGİSAYAR AYARI */
    @media (min-width: 769px) {{
        .main-container {{ top: 50%; transform: translateY(-50%); }}
        .mettot-header {{ font-size: 70px; margin-bottom: 30px; }}
        .my-button {{ font-size: 22px; padding: 15px 40px; width: 300px; }}
    }}

    /* MOBİL AYARI - FOTOĞRAFI ENGELLEMEYEN YENİ DÜZEN */
    @media (max-width: 768px) {{
        .main-container {{ 
            top: 35%; /* Çok daha aşağı aldık, senin baş hizandan uzak */
        }}
        .mettot-header {{ 
            font-size: 38px; 
            margin-bottom: 25px;
        }}
        .my-button {{ 
            font-size: 16px; 
            padding: 13px 0; 
            width: 80%; 
        }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="http://googleusercontent.com/spotify.com/5" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
