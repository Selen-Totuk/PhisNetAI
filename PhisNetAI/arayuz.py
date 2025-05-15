import streamlit as st
import joblib

# Modeli ve vectorizer'ı yükle
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

# Başlık
st.title("📧 PhishNetAI – Sahte E-posta Tespit Sistemi")
st.write("Bu sistem, yapay zeka ile e-postaların SAHTE (phishing) olup olmadığını analiz eder.")

# Kullanıcıdan e-posta metni al
eposta = st.text_area("✉️ E-posta içeriğini buraya yazın veya yapıştırın:")

# Butona basıldığında analiz et
if st.button("📌 Kontrol Et"):
    if eposta.strip() == "":
        st.warning("Lütfen bir e-posta metni girin.")
    else:
        # E-postayı vektöre çevir
        X_input = vectorizer.transform([eposta])
        tahmin = model.predict(X_input)

        # Sonucu göster
        if tahmin[0] == 1:
            st.error("🚨 SAHTE E-POSTA TESPİT EDİLDİ!")
        else:
            st.success("✅ GÜVENLİ E-POSTA")

# Ekstra: alt bilgi
st.caption("🔒 PhishNetAI, sahte bağlantı ve şüpheli dil kalıplarını analiz ederek çalışır.")
