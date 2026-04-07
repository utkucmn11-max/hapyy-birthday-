import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Mutlu Yıllar!", page_icon="🎉", layout="wide")

# Session State ile sayfa kontrolü (Butona basınca sayfa değişimi için)
if 'kutlama_basladi' not in st.session_state:
    st.session_state.kutlama_basladi = False

# --- CSS TASARIMI ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;700&display=swap');
    
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

    /* Giriş Kartı */
    .intro-card {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 60px;
        border-radius: 30px;
        border: 1px solid rgba(255,255,255,0.2);
        text-align: center;
        margin: auto;
        max-width: 600px;
        color: white;
    }

    /* Hareketli Yazı Efekti */
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
    
    .celebration-container {
        text-align: center;
        padding-top: 5vh;
        z-index: 10;
        position: relative;
    }

    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 6rem;
        color: #fff;
        text-shadow: 0 0 20px #ff00de, 0 0 30px #ff00de;
        animation: pulse 2s infinite;
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
    
    # Arka planda uçuşan "Happy Birthday" yazıları (Farklı konumlarda)
    for i in range(10):
        st.markdown(f'<div class="moving-text" style="top:{i*10}vh; left:{i*5}%; animation-delay:{i}s;">Happy Birthday {st.session_state.isim}! 🎂</div>', unsafe_allow_html=True)

    # Efektler (Aşağıdan balonlar ve yukarıdan konfeti)
    st.balloons() # Aşağıdan yukarı balonlar (Streamlit yerleşik)
    st.snow()     # Yukarıdan aşağı konfeti/kar efekti (Streamlit yerleşik)

    # Ana İçerik
    st.markdown('<div class="celebration-container">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="main-title">İyi ki Doğdun {st.session_state.isim}!</h1>', unsafe_allow_html=True)
    
    # Orta kısma büyük bir pasta veya kutlama GIF'i
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", width=600)
    
    st.markdown('<h2 style="color:white; font-family:Poppins;">Yeni yaşın sana tüm güzellikleri getirsin!</h2>', unsafe_allow_html=True)
    
    # Geri Dön Butonu
    if st.button("Başa Dön ↩️"):
        st.session_state.kutlama_basladi = False
        st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)

    # Arka planda coşkulu bir ses (Opsiyonel - Otomatik çalması tarayıcı engeline takılabilir)
    # st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
    
