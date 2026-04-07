import streamlit as st
import time

# Sayfa ayarları
st.set_page_config(page_title="Doğum Günü Kutlaması", page_icon="🎂")

# CSS ile biraz görsellik katalım
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
    }
    .celebration-text {
        text-align: center;
        color: #ff4b4b;
        font-family: 'Arial';
    }
    </style>
    """, unsafe_style_code=True)

st.title("🎂 Doğum Günü Özel Sayfası")
st.write("Bu linki paylaştığın kişi kendi adını yazarak kutlamayı görebilir.")

# Kullanıcıdan isim alma
isim = st.text_input("Lütfen ismini yazar mısın?", placeholder="Örn: Utku")

if st.button("Kutlamayı Başlat! 🎉"):
    if isim:
        with st.spinner('Pasta hazırlanıyor...'):
            time.sleep(2)
        
        # Konfeti efekti
        st.balloons()
        
        st.markdown(f"""
            <div class="celebration-text">
                <h1>İyi ki Doğdun {isim}! 🥳</h1>
                <p>Yeni yaşın sana sağlık, mutluluk ve başarı getirsin.</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Görsel veya bir kutlama mesajı
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif")
        
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3") # Örnek bir melodi
        
    else:
        st.warning("Lütfen kutlama için bir isim girin.")

# Alt bilgi
st.sidebar.info("Bu site sevdiklerinizin doğum gününü kutlamak için özel olarak tasarlandı.")