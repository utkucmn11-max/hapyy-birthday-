import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(page_title="Mutlu Yıllar!", layout="wide")

if 'kutlama' not in st.session_state:
    st.session_state.kutlama = False

# --- ÖZEL KONFETİ BİLEŞENİ ---
# Bu fonksiyon, tarayıcının engellemeyeceği şekilde konfeti fırlatır
def real_confetti():
    confetti_js = """
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
        function fire() {
            confetti({
                particleCount: 150,
                spread: 70,
                origin: { y: 0.6 },
                colors: ['#ff0000', '#00ff00', '#0000ff', '#ffff00', '#ff00ff', '#00ffff']
            });
        }
        // Sayfa her yüklendiğinde ve buton tıklandığında çalışması için
        setTimeout(fire, 100); 
    </script>
    """
    # scrolling=False ve height=0.1 ile "This is content" yazısını tamamen yok ediyoruz
    return components.html(confetti_js, height=0.1, scrolling=False)

# --- TASARIM ---
st.markdown("""
    <style>
    .stApp { background-color: #0f0c29; color: white; text-align: center; }
    .title { font-size: 5rem; font-family: 'Arial'; margin-top: 20vh; }
    .stButton>button { width: 100%; height: 60px; font-size: 1.5rem; border-radius: 30px; }
    </style>
    """, unsafe_allow_html=True)

# --- UYGULAMA ---
if not st.session_state.kutlama:
    st.markdown("<h1 class='title'>Sürprizi Açmaya Hazır mısın?</h1>", unsafe_allow_html=True)
    isim = st.text_input("İsim Yazınız", placeholder="Örn: Utku")
    if st.button("KUTLAMAYI BAŞLAT 🎉"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama = True
            st.rerun()
else:
    # KONFETİ BURADA TETİKLENİYOR
    real_confetti() 
    
    st.markdown(f"<h1 class='title'>İYİ Kİ DOĞDUN <br>{st.session_state.isim.upper()}!</h1>", unsafe_allow_html=True)
    
    # Gif'i tekrar ekliyoruz
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", use_column_width=True)
    
    if st.button("Tekrar Konfeti Patlat! 🎊"):
        st.rerun()
        
    if st.button("Geri Dön"):
        st.session_state.kutlama = False
        st.rerun()
