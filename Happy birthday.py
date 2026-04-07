import streamlit as st

st.set_page_config(layout="wide") # Sütunların sığması için ekranı genişletiyoruz

st.title("🎂 İsim Seçin veya Yazın")

# 1. Yöntem: Manuel İsim Girişi (Daha önce yaptığımız)
isim = st.text_input("Kutlanacak kişinin adını buraya yazın:")

st.divider()

# 2. Yöntem: 8 Sütunlu Hızlı Seçim Paneli
st.subheader("Hızlı Seçim (8 Sütunlu Izgara)")

# Örnek isim listesi (Burayı dilediğin kadar uzatabilirsin)
isimler = ["Utku", "Sude", "Ahmet", "Ayşe", "Mehmet", "Can", "Ece", "Deniz", "Mert", "Selin"]

# 8'li gruplara bölerek sütunları oluşturma
for i in range(0, len(isimler), 8):
    cols = st.columns(8) # Her satırda 8 sütun oluştur
    for j, name in enumerate(isimler[i:i+8]):
        with cols[j]:
            if st.button(name, key=f"btn_{name}_{i+j}"):
                isim = name # Butona basınca ismi kutlama alanına aktar

# Kutlama Alanı
if isim:
    st.balloons()
    st.success(f"### İyi ki doğdun **{isim}**! 🎉")
    st.write("Nice mutlu, sağlıklı ve huzurlu senelere...")
