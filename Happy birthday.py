import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları - Mobil tarayıcılar için tam uyum
st.set_page_config(page_title="İYİ Kİ DOĞDUN!", page_icon="🎂", layout="wide")

if 'kutlama_basladi' not in st.session_state:
    st.session_state.kutlama_basladi = False

# --- MOBİL OPTİMİZE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@900&display=swap');
    
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }

    /* Giriş Kartı - Mobilde Geniş */
    .intro-card {
        background: rgba(255, 255, 255, 0.15);
        backdrop-filter: blur(15px);
        padding: 30px;
        border-radius: 25px;
        text-align: center;
        margin: 5vh auto;
        width: 90%;
        color: white;
    }

    /* Dev Başlık - Mobilde Ekranı Kapatır */
    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 15vw; /* Ekran genişliğine göre büyür */
        color: #fff;
        text-shadow: 0 0 20px #ff00de, 0 0 40px #ff00de;
        text-align: center;
        line-height: 1.2;
        margin-bottom: 20px;
    }

    /* Hareketli Yazılar - Mobilde Daha Belirgin */
    .moving-text {
        position: fixed;
        font-family: 'Pacifico', cursive;
        font-size: 2rem;
        color: rgba(255, 255, 255, 0.3);
        z-index: 0;
        white-space: nowrap;
        animation: float 6s linear infinite;
        pointer-events: none;
    }

    /* Butonlar - Mobilde Dev Boyut */
    .stButton>button {
        width: 100% !important;
        height: 80px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        border-radius: 40px !important;
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%) !important;
        color: white !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    @keyframes float {
        from { transform: translateX(100%) translateY(0vh); }
        to { transform: translateX(-100%) translateY(100vh); }
    }

    /* Streamlit arayüzünü tamamen gizle */
    #MainMenu, footer, header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- KONFETİ (MOBİLDE KASMAZ) ---
def konfeti_yagdir():
    js = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        var end = Date.now() + (8 * 1000);
        (function frame() {
          confetti({ particleCount: 5, angle: 60, spread: 55, origin: { x: 0 }, colors: ['#ff00de', '#ffffff'] });
          confetti({ particleCount: 5, angle: 120, spread: 55, origin: { x: 1 }, colors: ['#00ffff', '#ffffff'] });
          if (Date.now() < end) { requestAnimationFrame(frame); }
        }());
    </script>
    """
    components.html(js, height=0)

# --- UYGULAMA ---
if not st.session_state.kutlama_basladi:
    st.markdown('<div class="intro-card">', unsafe_allow_html=True)
    st.markdown("<h1 style='font-size: 2.5rem;'>DOĞUM GÜNÜ PORTALI 🎂</h1>", unsafe_allow_html=True)
    st.write("İsmini yaz ve sürprizi gör!")
    isim = st.text_input("", placeholder="Buraya yaz...", label_visibility="collapsed")
    if st.button("KUTLAMAYI BAŞLAT! 🚀"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_basladi = True
            st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

else:
    konfeti_yagdir()
    st.balloons()

    # Arka planda uçan yazılar
    for i in range(8):
        st.markdown(f'<div class="moving-text" style="top:{i*12}vh; animation-delay:{i}s;">İYİ Kİ DOĞDUN {st.session_state.isim.upper()}!</div>', unsafe_allow_html=True)

    # İçerik Alanı
    st.markdown(f'<div class="main-title">İyi ki Doğdun<br>{st.session_state.isim}!</div>', unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", use_column_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("TEKRAR PATLAT! 🎊"):
        st.rerun()
    
    st.write("") # Boşluk
    
    if st.button("GERİ DÖN ↩️"):
        st.session_state.kutlama_basladi = False
        st.rerun()
