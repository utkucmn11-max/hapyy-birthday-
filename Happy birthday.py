import streamlit as st
import time

# Sayfa Konfigürasyonu
st.set_page_config(
    page_title="Mutlu Yıllar | Özel Kutlama",
    page_icon="🎁",
    layout="centered"
)

# Gelişmiş CSS (Profesyonel Arayüz Tasarımı)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Poppins', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }

    .main-card {
        background: rgba(255, 255, 255, 0.95);
        padding: 50px;
        border-radius: 30px;
        box-shadow: 0 20px 40px rgba(0,0,0,0.2);
        text-align: center;
        margin-top: 20px;
    }

    .celebration-title {
        background: -webkit-linear-gradient(#764ba2, #667eea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 800;
        font-size: 3.5rem;
        margin-bottom: 10px;
    }

    .stButton>button {
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%);
        color: white;
        border: none;
        padding: 15px 40px;
        border-radius: 50px;
        font-weight: 600;
        letter-spacing: 1px;
        transition: all 0.3s ease;
        width: 100%;
    }

    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 10px 20px rgba(255, 75, 43, 0.3);
    }
    
    .name-input input {
        border-radius: 15px !important;
        text-align: center;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Arayüz Başlangıcı ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.markdown('<h1 style="color: #1E1E1E; font-size: 1.5rem; font-weight: 300;">Özel Bir Gün, Özel Bir Kutlama</h1>', unsafe_allow_html=True)
st.markdown('<div class="celebration-title">HOŞ GELDİN</div>', unsafe_allow_html=True)

# Giriş Alanı
st.markdown('<div class="name-input">', unsafe_allow_html=True)
isim = st.text_input("", placeholder="İsmini buraya yazarak başla...", label_visibility="collapsed")
st.markdown('</div>', unsafe_allow_html=True)

if isim:
    st.write("")
    if st.button("KUTLAMAYI AÇ ✨"):
        # Profesyonel Yükleme Sekansı
        progress_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            progress_bar.progress(percent_complete + 1)
        
        st.balloons()
        
        # Kutlama İçeriği
        st.markdown(f"""
            <div style="margin-top: 30px;">
                <h1 style="color: #1E1E1E; font-size: 2.5rem;">İyi ki Doğdun, <span style="color: #764ba2;">{isim}!</span> 🎂</h1>
                <p style="color: #555; font-size: 1.1rem; line-height: 1.6;">
                    Bugün senin günün. Yeni yaşının sana en az senin kadar güzel <br> 
                    sürprizler, sonsuz mutluluk ve başarı getirmesini dilerim.
                </p>
            </div>
        """, unsafe_allow_html=True)
        
        # Profesyonel bir kutlama GIF'i (Veya Lottie linki)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif")
        
        # Şık bir ses efekti (Opsiyonel)
        # st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="text-align: center; margin-top: 30px; color: rgba(255,255,255,0.7); font-size: 0.8rem; letter-spacing: 2px;">
        DESIGNED BY UTKU • 2026
    </div>
""", unsafe_allow_html=True)
