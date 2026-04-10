import streamlit as st

# Sayfa ayarlarını ve ikonunu en başta belirle
st.set_page_config(page_title="Mettot-Sx", layout="wide")

# CSS - Hız için optimize edildi
st.markdown("""
    <style>
    /* Gereksiz Streamlit öğelerini tamamen yok et */
    header, footer, .stDeployButton {display: none !important;}
    .block-container {padding: 0px !important;}
    
    .stApp {
        /* BURAYA ImgBB'DEN ALDIĞIN DİREKT LİNKİ YAPIŞTIRIRSAN ÇOK DAHA HIZLI OLUR */
        /* Örnek: url("https://i.ibb.co/xxxx/arka-plan.webp") */
        background: linear-gradient(rgba(0, 0, 0, 0.4), rgba(0, 0, 0, 0.4)),
                    url("https://raw.githubusercontent.com/alidnr/Mettot-web/main/arka_plan.webp");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        height: 100vh;
    }

    .main-container {
        position: fixed;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%);
        width: 100%;
        text-align: center;
        display: flex;
        flex-direction: column;
        align-items: center;
    }

    .mettot-header {
        color: white;
        font-family: 'Courier New', monospace;
        font-size: 80px;
        font-weight: bold;
        text-shadow: 2px 2px 20px rgba(0,0,0,1);
        margin-bottom: 30px;
        letter-spacing: 5px;
    }

    .my-button {
        background-color: rgba(255, 255, 255, 0.1);
        color: white !important;
        border: 1px solid rgba(255, 255, 255, 0.4);
        border-radius: 15px;
        text-decoration: none !important;
        font-weight: bold;
        padding: 18px 0;
        width: 350px;
        margin: 10px auto;
        display: block;
        transition: 0.3s;
        backdrop-filter: blur(8px);
    }

    .my-button:hover {
        background-color: rgba(255, 255, 255, 0.2);
        transform: scale(1.05);
        box-shadow: 0px 0px 20px rgba(255, 255, 255, 0.3);
    }

    /* Mobil Ayarı */
    @media (max-width: 768px) {
        .mettot-header { font-size: 45px; }
        .my-button { width: 80%; padding: 15px 0; }
    }
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <a href="https://open.spotify.com/artist/6xi4UQoVjPLTld9Fu12736?si=xne1GWFqQQeQaEJV5alviQ" target="_blank" class="my-button">Spotify</a>
        <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
        <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
    </div>
""", unsafe_allow_html=True)
