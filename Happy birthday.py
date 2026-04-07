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
    
    /* Yazıları ortalayan ve boyutu biraz ufaltılmış başlık */
    .dev-baslik {
        font-family: 'Poppins', sans-serif;
        font-size: 10vw; /* 12vw'den 10vw'ye çekildi */
        text-align: center;
        text-shadow: 2px 2px 10px rgba(0,0,0,0.3);
        margin-top: 20px;
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
    }
    
    /* Alt başlık ve mesajlar için ortalama */
    .alt-mesaj {
        text-align: center;
        width: 100%;
        margin-top: 10px;
        font-size: 1.5rem; /* Boyut mobilde daha okunabilir yapıldı */
    }

    /* Giriş ekranı yazıları */
    .giris-text {
        font-size: 2.2rem; /* 3rem'den ufaltıldı */
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Mobilde Butonu Dev Yap */
    .stButton>button {
        width: 100% !important;
        height: 70px !important; /* 80'den 70'e çekildi */
        font-size: 1.3rem !important; /* Biraz ufaltıldı */
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

    /* Resim ortalama */
    .stImage {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- UYGULAMA AKIŞI ---

if not st.session_state.kutlama_aktif:
    # GİRİŞ EKRANI
    st.markdown("<div style='text-align:center; padding-top:15vh;'>", unsafe_allow_html=True)
    st.markdown("<h1 class='giris-text'>SANA BİR MESAJ VAR! 💌</h1>", unsafe_allow_html=True)
    
    # Text input'u ortalamak için boşluklar kullanabiliriz veya CSS ile input stiline dokunabiliriz
    isim = st.text_input("", placeholder="İsmini buraya yaz...", label_visibility="collapsed")
    
    if st.button("MESAJI AÇ! 🔥"):
        if isim:
            st.session_state.isim = isim
            st.session_state.kutlama_aktif = True
            st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)

else:
    # KUTLAMA EKRANI
    
    # 1. Balonlar
    st.balloons()
    
    # 2. Devasa İsim Yazısı (Boyutu ufaltıldı ve ortalandı)
    st.markdown(f'<div class="dev-baslik">İYİ Kİ DOĞDUN<br>{st.session_state.isim.upper()}!</div>', unsafe_allow_html=True)
    
    # 3. Dev Hareketli GIF
    st.image("https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjN4eTBvcWJleXIwNGZla21tbWc5NHc5NTllcDl5c3VsbG90ZG4xOSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rMsV3D1Fb7u2Va6KpC/giphy.gif", use_column_width=True)
    
    st.markdown("<h2 class='alt-mesaj'>Yeni yaşın kutlu olsun! ✨</h2>", unsafe_allow_html=True)
    
    # Alt Butonlar
    st.write("") # Küçük bir boşluk
    if st.button("TEKRAR BALON UÇUR! 🎈"):
        st.rerun()
        
    if st.button("BAŞA DÖN ↩️"):
        st.session_state.kutlama_aktif = False
        st.rerun()
