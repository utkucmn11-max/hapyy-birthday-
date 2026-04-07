import streamlit as st

# Sayfa ayarları - Mobilde büyük görünmesi için
st.set_page_config(page_title="İYİ Kİ DOĞDUN!", page_icon="🎂", layout="wide")

# Kutlama durumunu kontrol etme
if 'kutlama_aktif' not in st.session_state:
    st.session_state.kutlama_aktif = False

# --- ŞIK VE BÜYÜK TASARIM (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@900&display=swap');
    
    .stApp {
        background: linear-gradient(135deg, #FF416C 0%, #FF4B2B 100%);
        color: white;
    }
    
    .dev-baslik {
        font-family: 'Poppins', sans-serif;
        font-size: 12vw;
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        margin-top: 20px;
    }
    
    /* Mobilde Butonu Dev Yap */
    .stButton>button {
        width: 100% !important;
        height: 80px !important;
        font-size: 1.5rem !important;
        font-weight: bold !important;
        border-radius: 40px !important;
        background-color: white !important;
        color: #FF416C !important;
        border: none !important;
        box-shadow: 0 10px 20px rgba(0,0,0,0.2) !important;
    }
    
    /* Streamlit yazılarını gizle */
    footer {visibility: hidden;}
    header {visibility: hidden;}
    </style>
    """, unsafe_allow_html=True)

# --- UYGULAMA AKIŞI ---

if not st.session_state.kutlama_aktif:
    # GİRİŞ EKRANI
    st.markdown("<div style='text-align:center; padding-top:15vh;'>", unsafe_allow_html=True)
    st.markdown("<h1 style='font-size:3rem;'>SANA BİR MESAJ VAR! 💌</h1>", unsafe_allow_html=True)
    
    isim = st.text_input("", placeholder="İsmini buraya yaz...", label_visibility="collapsed")
    
    if st.button("MESAJI AÇ! 🔥"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_aktif = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # KUTLAMA EKRANI (Hata verme ihtimali sıfır olan kısım)
    
    # 1. Balonlar (Bu her cihazda kesin çalışır)
    st.balloons()
    
    # 2. Devasa İsim Yazısı
    st.markdown(f'<div class="dev-baslik">İYİ Kİ DOĞDUN<br>{st.session_state.isim.upper()}!</div>', unsafe_allow_html=True)
    
    # 3. Dev Hareketli GIF (Kutlama gifi)
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", use_column_width=True)
    
    st.markdown("<h2 style='text-align:center;'>Yeni yaşın kutlu olsun! ✨</h2>", unsafe_allow_html=True)
    
    # Alt Butonlar
    if st.button("TEKRAR BALON UÇUR! 🎈"):
        st.rerun()
        
    if st.button("BAŞA DÖN ↩️"):
        st.session_state.kutlama_aktif = False
        st.rerun()
