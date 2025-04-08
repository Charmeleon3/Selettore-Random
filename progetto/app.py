import streamlit as st
import random
import os

# Titolo app
st.title("🎲 Selettore di immagini locali")

# Percorso alla cartella con le immagini
IMAGES_FOLDER = "C:\\Users\\LucarioNervi\\Desktop\\progetto\\immagini"

# Carica la lista di immagini all'avvio
if 'pool' not in st.session_state:
    immagini = [os.path.join(IMAGES_FOLDER, f) for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    st.session_state.pool = immagini.copy()

# Mostra quante immagini restano
st.write(f"Immagini rimanenti: {len(st.session_state.pool)}")

# Bottone per estrarre
if st.button("Estrai immagine"):
    if st.session_state.pool:
        scelta = random.choice(st.session_state.pool)
        st.image(scelta, caption="Immagine selezionata")
        st.session_state.pool.remove(scelta)
    else:
        st.warning("Hai esaurito le immagini!")

# Bottone per reset
if st.button("Reset pool"):
    immagini = [os.path.join(IMAGES_FOLDER, f) for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    st.session_state.pool = immagini.copy()
    st.success("Pool resettato!")
