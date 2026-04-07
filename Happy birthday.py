import streamlit as st
import streamlit.components.v1 as components
import time

# Sayfa ayarları
st.set_page_config(page_title="Mutlu Yıllar!", page_icon="🎉", layout="wide")

# Session State kontrolü
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

    .moving-text {
        position: fixed;
        font-family: 'Pacifico', cursive;
        font-size: 2.5rem;
        color: rgba(255, 255, 255, 0.4);
        z-index: 0;
        white-space: nowrap;
        animation: float 10s linear infinite;
        pointer-events: none;
    }
    
    @keyframes float {
        from { transform: translateX(110%) translateY(0vh) rotate(0deg); }
        to { transform: translateX(-110%) translateY(100vh) rotate(360deg); }
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

# --- GERÇEK KONFETİ FONKSİYONU ---
def konfeti_yagdir():
    # JavaScript ile gerçek renkli konfeti efekti
    components.html(
        """
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            var end = Date.now() + (5 * 1000); // 5 saniye boyunca yağdır
            var colors = ['#ff00de', '#ff4b4b', '#fdbb2d', '#ffffff', '#667eea'];

            (function frame() {
              confetti({
                particleCount: 3,
                angle: 60,
                spread: 55,
                origin: { x: 0 },
                colors: colors
              });
              confetti({
                particleCount: 3,
                angle: 120,
                spread: 55,
                origin: { x: 1 },
                colors: colors
              });

              if (Date.now() < end) {
                requestAnimationFrame(frame);
              }
            }());
        </script>
        """,
        height=0,
    )

# --- SAYFA MANTIĞI ---

if not st.session_state.kutlama_basladi:
    st.write("")
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
    
    # 1. Gerçek Konfetiler (Yukarıdan ve yanlardan renkli yağar)
    konfeti_yagdir()
    
    # 2. Balonlar (Aşağıdan yukarı çıkar)
    st.balloons() 

    # Arka planda uçuşan yazılar
    for i in range(10):
        st.markdown(f'<div class="moving-text" style="top:{i*10}vh; left:{i*5}%; animation-delay:{i}s;">Happy Birthday {st.session_state.isim}! 🎂</div>', unsafe_allow_html=True)

    # Ana İçerik
    st.markdown('<div class="celebration-container">', unsafe_allow_html=True)
    st.markdown(f'<h1 class="main-title">İyi ki Doğdun {st.session_state.isim}!</h1>', unsafe_allow_html=True)
    
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", width=600)
    
    st.markdown(f'<h2 style="color:white; font-family:Poppins;">{st.session_state.isim}, yeni yaşın sana tüm güzellikleri getirsin!</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1,1])
    with col2:
        if st.button("Tekrar Patlat! 🎊"):
            st.rerun()
        if st.button("Başa Dön ↩️"):
            st.session_state.kutlama_basladi = False
            st.rerun()
        
    st.markdown('</div>', unsafe_allow_html=True)
