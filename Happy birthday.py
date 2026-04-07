import streamlit as st
import streamlit.components.v1 as components
import time

# Sayfa ayarları
st.set_page_config(page_title="Mutlu Yıllar!", page_icon="🎊", layout="wide")

if 'kutlama_basladi' not in st.session_state:
    st.session_state.kutlama_basladi = False

# --- ÖZEL KONFETİ VE TASARIM (CSS/JS) ---
def konfeti_patlat():
    # Bu JavaScript kodu ekrana gerçek renkli konfetiler yağdırır
    components.html(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            var count = 200;
            var defaults = { origin: { y: 0.7 } };

            function fire(particleRatio, opts) {
              confetti(Object.assign({}, defaults, opts, {
                particleCount: Math.floor(count * particleRatio)
              }));
            }

            fire(0.25, { spread: 26, startVelocity: 55 });
            fire(0.2, { spread: 60 });
            fire(0.35, { spread: 100, decay: 0.91, scalar: 0.8 });
            fire(0.1, { spread: 120, startVelocity: 25, decay: 0.92, scalar: 1.2 });
            fire(0.1, { spread: 120, startVelocity: 45 });
        </script>
        """,
        height=0,
    )

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Pacifico&family=Poppins:wght@400;700&display=swap');
    
    .stApp {
        background: #0f0c29;
        background: -webkit-linear-gradient(to right, #24243e, #302b63, #0f0c29);
        background: linear-gradient(to right, #24243e, #302b63, #0f0c29);
    }

    .intro-card {
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(15px);
        padding: 50px;
        border-radius: 40px;
        border: 1px solid rgba(255,255,255,0.1);
        text-align: center;
        margin: 100px auto;
        max-width: 500px;
        color: white;
        box-shadow: 0 25px 50px rgba(0,0,0,0.5);
    }

    .main-title {
        font-family: 'Pacifico', cursive;
        font-size: 5rem;
        background: linear-gradient(to right, #ff00cc, #3333ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: glow 2s ease-in-out infinite alternate;
    }

    @keyframes glow {
        from { filter: drop-shadow(0 0 10px #ff00cc); }
        to { filter: drop-shadow(0 0 20px #3333ff); }
    }

    .flying-text {
        position: fixed;
        color: rgba(255,255,255,0.2);
        font-size: 20px;
        pointer-events: none;
        white-space: nowrap;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MANTIK ---

if not st.session_state.kutlama_basladi:
    st.markdown('<div class="intro-card">', unsafe_allow_html=True)
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=100)
    st.markdown("<h2 style='margin-bottom:20px;'>Doğum Günü Portalı</h2>", unsafe_allow_html=True)
    
    isim = st.text_input("", placeholder="Kimin ismi yazılsın?", label_visibility="collapsed")
    
    if st.button("SÜRPRİZİ BAŞLAT 🎉"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_basladi = True
            st.rerun()
        else:
            st.error("Lütfen bir isim yaz!")
    st.markdown('</div>', unsafe_allow_html=True)

else:
    # Sayfa açılır açılmaz konfeti ve balonları tetikle
    konfeti_patlat()
    st.balloons() 

    # Ekranda uçuşan yazılar
    for i in range(15):
        st.markdown(f'<div class="flying-text" style="top:{i*7}%; left:{i*3}%; opacity:0.3;">HAPPY BIRTHDAY {st.session_state.isim.upper()}!</div>', unsafe_allow_html=True)

    # Ana İçerik Sayfası
    st.markdown("<div style='text-align:center; padding-top:10vh;'>", unsafe_allow_html=True)
    st.markdown(f'<h1 class="main-title">İyi ki Doğdun {st.session_state.isim}!</h1>', unsafe_allow_html=True)
    
    # Çok daha "cana yakın" bir görsel
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", width=500)
    
    st.markdown(f"<h3 style='color:white; font-family:Poppins;'>{st.session_state.isim}, yeni yaşında her şey gönlünce olsun! 🚀</h3>", unsafe_allow_html=True)
    
    if st.button("Tekrar Patlat! 🎊"):
        st.rerun() # Sayfayı yenileyerek konfetileri tekrar atar

    if st.button("Ana Sayfaya Dön"):
        st.session_state.kutlama_basladi = False
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)
