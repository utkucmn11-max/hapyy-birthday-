import streamlit as st
import streamlit.components.v1 as components
import time

# Sayfa ayarları - Ekranın tamamını kullanıyoruz
st.set_page_config(page_title="MUTLU YILLAR!", page_icon="🔥", layout="wide")

if 'kutlama_basladi' not in st.session_state:
    st.session_state.kutlama_basladi = False

# --- DEVASA CSS TASARIMI ---
st.markdown("""
    <style>
    
    /* Arka Plan Animasyonu */
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Giriş Kartı - Daha Büyük */
    .intro-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(20px);
        padding: 80px;
        border-radius: 50px;
        text-align: center;
        margin: 10vh auto;
        max-width: 800px;
        color: white;
        border: 2px solid rgba(255,255,255,0.3);
    }

    /* Uçuşan Yazılar - Daha Belirgin */
    .moving-text {
        position: fixed;
        font-family: 'Pacifico', cursive;
        font-size: 4rem; /* Dev font */
        color: rgba(255, 255, 255, 0.3);
        z-index: 0;
        white-space: nowrap;
        animation: float 8s linear infinite;
        pointer-events: none;
    }
    
    @keyframes float {
        from { transform: translateX(120%) translateY(0vh) rotate(-10deg); }
        to { transform: translateX(-120%) translateY(100vh) rotate(10deg); }
    }

    /* Ana Başlık - DEVASE */
    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 8rem; /* EKRANI KAPLAYAN BAŞLIK */
        color: #fff;
        text-shadow: 0 0 30px #ff00de, 0 0 60px #ff00de, 0 0 90px #ff00de;
        margin-top: -50px;
    }

    /* Butonları büyütme */
    .stButton>button {
        font-size: 2rem !important;
        padding: 20px 50px !important;
        border-radius: 100px !important;
    }
    
    /* Streamlit'in kendi yazılarını gizle */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- GÜÇLENDİRİLMİŞ KONFETİ ---
def konfeti_yagdir():
    confetti_js = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        var end = Date.now() + (10 * 1000); // 10 SANİYE BOYUNCA YAĞDIR
        (function frame() {
          confetti({ particleCount: 7, angle: 60, spread: 70, origin: { x: 0 }, colors: ['#ff00de', '#ffffff'] });
          confetti({ particleCount: 7, angle: 120, spread: 70, origin: { x: 1 }, colors: ['#00ffff', '#ffffff'] });
          if (Date.now() < end) { requestAnimationFrame(frame); }
        }());
    </script>
    """
    # "This is content" yazısını engellemek için bileşeni gizliyoruz
    components.html(confetti_js, height=0, width=0)

# --- MANTIK ---
if not st.session_state.kutlama_basladi:
    st.markdown('<div class="intro-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 4rem;'>HAZIR MISIN? 🚀</h1>", unsafe_allow_html=True)
    isim = st.text_input("", placeholder="İsim Giriniz...", label_visibility="collapsed")
    if st.button("KUTLAMAYI PATLAT! 🔥"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_basladi = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    konfeti_yagdir() # JavaScript konfeti
    st.balloons()    # Balonlar
    
    # Ekranda Dev Uçuşan Yazılar
    for i in range(12):
        st.markdown(f'<div class="moving-text" style="top:{i*8}vh; animation-delay:{i*0.5}s;">HAPPY BIRTHDAY {st.session_state.isim.upper()}! 🎂</div>', unsafe_allow_html=True)

    st.markdown('<div style="text-align:center; position:relative; z-index:10;">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="main-title">{st.session_state.isim}!</h1>', unsafe_allow_html=True)
    
    # Dev Görsel
    
    st.markdown(f"<h1 style='color:white; font-size:3rem;'>İYİ Kİ DOĞDUN! 🎉</h1>", unsafe_allow_html=True)
    
    if st.button("TEKRAR PATLAT 🎊"):
        st.rerun()
    
    if st.button("BAŞA DÖN"):
        st.session_state.kutlama_basladi = False
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)
