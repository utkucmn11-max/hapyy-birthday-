import streamlit as st
import time

# Sayfa ayarları - Mobilde büyük görünmesi için 'wide' düzen
st.set_page_config(page_title="Mutlu Yıllar!", page_icon="🎉", layout="wide")

# Session State ile sayfa kontrolü (Butona basınca sayfa değişimi için)
if 'kutlama_basladi' not in st.session_state:
    st.session_state.kutlama_basladi = False

# --- CSS TASARIMI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;700&display=swap');
    
    /* Hareketli Arka Plan */
    .stApp {
        background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Giriş Kartı - Mobilde Büyük */
    .intro-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 50px;
        border-radius: 30px;
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
        margin: auto;
        max-width: 600px;
        color: white;
    }

    /* Ekranda Uçuşan Yazılar */
    .moving-text {
        position: fixed;
        font-family: 'Pacifico', cursive;
        font-size: 2.5rem;
        color: rgba(255, 255, 255, 0.6);
        z-index: 0;
        white-space: nowrap;
        animation: float 10s linear infinite;
    }
    
    @keyframes float {
        from { transform: translateX(100%) translateY(0vh) rotate(0deg); }
        to { transform: translateX(-100%) translateY(100vh) rotate(360deg); }
    }
    
    /* Kutlama İçerik Alanı */
    .celebration-container {
        text-align: center;
        padding-top: 5vh;
        z-index: 10;
        position: relative;
    }

    /* Dev Neon Başlık */
    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 10vw; /* Ekrana göre büyüyen font */
        color: #fff;
        text-shadow: 0 0 20px #ff00de, 0 0 30px #ff00de;
        animation: pulse 2s infinite;
        margin-bottom: 20px;
    }

    /* Mobilde Büyük Butonlar */
    .stButton>button {
        width: 100% !important;
        height: 60px !important;
        font-size: 1.2rem !important;
        border-radius: 30px !important;
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%) !important;
        color: white !important;
        border: none !important;
    }

    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.05); }
        100% { transform: scale(1); }
    }
    </style>
    """, unsafe_allow_html=True)

# --- SAYFA MANTIĞI ---

if not st.session_state.kutlama_basladi:
    # --- GİRİŞ SAYFASI ---
    st.write("") # Boşluk
    st.write("")
    st.markdown('<div class="intro-card">', unsafe_allow_html=True)
    st.markdown("<h1>Hoş Geldin ✨</h1>", unsafe_allow_html=True)
    st.markdown("<p>Bugün kutlanacak özel bir şey var...</p>", unsafe_allow_html=True)
    
    isim = st.text_input("", placeholder="İsmini buraya yazar mısın?", label_visibility="collapsed")
    
    if st.button("KUTLAMAYI AÇ 🎁"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_basladi = True
            st.rerun()
        else:
            st.warning("Lütfen bir isim gir.")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # --- KUTLAMA SAYFASI ---
    
    # 1. Efektler (Aşağıdan balonlar ve yukarıdan kar tanesi konfetiler)
    st.balloons() # Aşağıdan yukarı balonlar
    st.snow()     # Yukarıdan aşağı kar tanesi (Streamlit yerleşik)

    # Arka planda uçuşan "Happy Birthday" yazıları
    for i in range(10):
        st.markdown(f'<div class="moving-text" style="top:{i*10}vh; left:{i*5}%; animation-delay:{i}s;">Happy Birthday {st.session_state.isim}! 🎂</div>', unsafe_allow_html=True)

    # Ana İçerik
    st.markdown('<div class="celebration-container">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="main-title">İyi ki Doğdun {st.session_state.isim}!</h1>', unsafe_allow_html=True)
    
    # --- GİF BURAYA EKLENDİ (Tam İstediğin Yer) ---
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", use_column_width=True)
    
    st.markdown(f'<h2 style="color:white; font-family:Poppins;">Yeni yaşın sana tüm güzellikleri getirsin!</h2>', unsafe_allow_html=True)
    
    # Boşluk ve Geri Dön Butonu
    st.write("") 
    if st.button("GERİ DÖN ↩️"):
        st.session_state.kutlama_basladi = False
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)
