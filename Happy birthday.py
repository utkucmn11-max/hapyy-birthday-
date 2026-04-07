import streamlit as st
import streamlit.components.v1 as components

# Sayfa ayarları
st.set_page_config(page_title="DOĞUM GÜNÜ!", page_icon="🎂", layout="wide")

if 'kutlama_basladi' not in st.session_state:
    st.session_state.kutlama_basladi = False

# --- CSS VE TASARIM ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@900&display=swap');
    
    .stApp {
        background: linear-gradient(-45deg, #ee7752, #e73c7e, #23a6d5, #23d5ab);
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }

    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 15vw;
        color: #fff;
        text-shadow: 0 0 20px #ff00de;
        text-align: center;
        margin-top: 20px;
    }

    /* Mobilde Butonları Dev Yap */
    .stButton>button {
        width: 100% !important;
        height: 70px !important;
        font-size: 1.5rem !important;
        border-radius: 35px !important;
        background: linear-gradient(90deg, #FF416C 0%, #FF4B2B 100%) !important;
        color: white !important;
        border: none !important;
    }

    /* Gereksiz yazıları gizle */
    #MainMenu, footer, header {visibility: hidden;}
    
    /* Konfeti alanındaki 'This is content' yazısını gizlemek için */
    iframe { border: none !important; }
    </style>
    """, unsafe_allow_html=True)

# --- GARANTİ KONFETİ FONKSİYONU ---
def konfeti_fiskirt():
    # Bu script doğrudan çalışır ve kütüphaneyi güvenli kaynaktan çeker
    js_code = """
    <div id="confetti-container"></div>
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function startConfetti() {
            var end = Date.now() + (7 * 1000);
            var colors = ['#bb0000', '#ffffff', '#ff00de', '#00ffff'];

            (function frame() {
              confetti({
                particleCount: 4,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: colors
              });
              confetti({
                particleCount: 4,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: colors
              });

              if (Date.now() < end) {
                requestAnimationFrame(frame);
              }
            }());
        }
        // Sayfa yüklendiği an başlat
        setTimeout(startConfetti, 100);
    </script>
    """
    # height=0.1 yaparak hem görünmez kılıyoruz hem de çalışmasını sağlıyoruz
    components.html(js_code, height=0.1)

# --- UYGULAMA AKIŞI ---
if not st.session_state.kutlama_basladi:
    st.markdown("<div style='text-align:center; color:white; padding-top:10vh;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:3rem;'>HOŞ GELDİN! ✨</h1>", unsafe_allow_html=True)
    isim = st.text_input("", placeholder="Kimin doğum günü?", label_visibility="collapsed")
    if st.button("KUTLAMAYI AÇ! 🚀"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_basladi = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # Konfetiyi tetikle
    konfeti_fiskirt()
    st.balloons() # Aşağıdan yukarı balonlar her zaman çalışır

    # İçerik
    st.markdown(f'<div class="main-title">{st.session_state.isim}!</div>', unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", use_column_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    if st.button("TEKRAR PATLAT! 🎊"):
        st.rerun()
    
    if st.button("GERİ DÖN"):
        st.session_state.kutlama_basladi = False
        st.rerun()
