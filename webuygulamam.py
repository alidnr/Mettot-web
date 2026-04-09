# --- TASARIM VE KESİN MERKEZLEME (CSS) ---
st.markdown(f"""
    <style>
    header, footer, .stDeployButton {{visibility: hidden !important;}}
    
    .stApp {{
        background-image: url("data:image/jpeg;base64,{bin_str if bin_str else ""}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed; /* Mobilde fotoğrafın kaymasını engeller */
    }}

    .main-container {{
        position: fixed;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        text-align: center;
        width: 90%; /* Mobilde kenarlardan boşluk bırakır */
        z-index: 10;
    }}

    /* BİLGİSAYAR İÇİN AYARLAR (Büyük Ekran) */
    .mettot-header {{
        color: white;
        font-size: 80px; 
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        margin-bottom: 30px;
        text-shadow: 5px 5px 20px rgba(0,0,0,1);
    }}

    .my-button {{
        background-color: rgba(0,0,0,0.7);
        color: white !important;
        padding: 15px 35px;
        border: 2px solid white;
        border-radius: 12px;
        text-decoration: none !important;
        font-size: 24px;
        font-weight: bold;
        display: inline-block;
        margin: 10px;
        transition: 0.3s;
    }}

    /* MOBİL İÇİN ÖZEL AYARLAR (Ekran 768px'den küçükse burası çalışır) */
    @media only screen and (max-width: 768px) {{
        .mettot-header {{
            font-size: 45px; /* Başlığı mobilde küçülttük ki sığsın */
        }}
        .my-button {{
            font-size: 18px; /* Buton yazılarını küçülttük */
            padding: 12px 25px;
            display: block; /* Butonları alt alta sıralar (daha kolay tıklanır) */
            margin: 10px auto;
            width: 80%; /* Butonlar genişlesin */
        }}
    }}
    </style>

    <div class="main-container">
        <div class="mettot-header">< METTOT ></div>
        <div class="button-group">
            <a href="http://spotify.com" target="_blank" class="my-button">Spotify</a>
            <a href="https://www.instagram.com/enessjordan" target="_blank" class="my-button">Instagram</a>
            <a href="https://youtube.com/@mettot-sx" target="_blank" class="my-button">YouTube</a>
        </div>
    </div>
""", unsafe_allow_html=True)
