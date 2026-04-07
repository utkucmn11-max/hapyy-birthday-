import streamlit as st
import time

# Sayfa Genişliği ve Başlık
st.set_page_config(page_title="Mutlu Yıllar!", page_icon="✨", layout="centered")

# Profesyonel Görünüm için CSS Dokunuşları
st.markdown("""
    <style>
    /* Arka plan ve genel yazı tipi */
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stApp {
        background: transparent;
    }
    
    /* Kart tasarımı */
    .birthday-card {
        background-color: white;
        padding: 40px;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        text-align: center;
        border-top: 5px solid #FF4B4B;
    }
    
    h1 {
        color: #1E1E1E;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
    }
    
    .subtitle {
        color: #555;
        font-size: 1.2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Başlık Kısmı
st.markdown('<div class="birthday-card">', unsafe_allow_html=True)
st.title("✨ Özel Bir Kutlama")
st.markdown('<p class="subtitle">Bu sayfa bugün doğan o özel kişi için hazırlandı.</p>', unsafe_allow_html=True)

# Giriş Alanı
isim = st.text_input("", placeholder="Buraya ismini yazar mısın? 😊", help="Kimin doğum gününü kutluyoruz?")

if isim:
    st.divider()
    if st.button(f"Hazırsan Tıkla, {isim}! 🎉"):
        # Küçük bir yükleme efekti (Profesyonel hava katar)
        with st.status("Senin için bir şeyler hazırlanıyor...", expanded=False) as status:
            time.sleep(1)
            st.write("Pastalar fırından çıktı...")
            time.sleep(1)
            st.write("Konfetiler dolduruldu...")
            status.update(label="Her şey hazır!", state="complete", expanded=False)
        
        st.balloons()
        
        # Kutlama Mesajı
        st.markdown(f"""
            <div style="text-align: center; padding: 20px;">
                <h1 style="font-size: 3rem; color: #FF4B4B;">İyi ki Doğdun {isim}! 🎂</h1>
                <p style="font-size: 1.5rem; color: #333;">Yeni yaşın sana tüm güzellikleri beraberinde getirsin.</p>
                <p style="font-style: italic; color: #777;">"Her günün bir kutlama tadında geçsin."</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Şık bir görsel (Giphy üzerinden kaliteli bir kutlama)
        st.image("https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHJueXZueXJueXZueXJueXZueXJueXZueXJueXZueXJueXZueCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/L95W4wv8nNbz072CC6/giphy.gif", use_column_width=True)
        
        # İstersen buraya bir kutlama müziği ekleyebilirsin
        # st.audio("muzik_linki.mp3")

st.markdown('</div>', unsafe_allow_html=True)

# Alt Bilgi
st.markdown("""
    <div style="text-align: center; margin-top: 50px; color: #888; font-size: 0.8rem;">
        Sevgiyle hazırlandı • 2026
    </div>
""", unsafe_allow_html=True)
