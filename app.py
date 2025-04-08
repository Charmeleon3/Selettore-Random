import streamlit as st
import random
import os

st.title("🎲 Selettore di immagini")

IMAGES_FOLDER = "immagini"

# Verifica se la cartella esiste
if 'pool' not in st.session_state:
    if not os.path.exists(IMAGES_FOLDER):
        st.error(f"La cartella '{IMAGES_FOLDER}' non è stata trovata. Verifica che sia presente nella root del repo.")
    else:
        immagini = [os.path.join(IMAGES_FOLDER, f) for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        st.session_state.pool = immagini.copy()

st.write(f"Immagini rimanenti: {len(st.session_state.pool)}")

if st.button("Estrai immagine"):
    if st.session_state.pool:
        scelta = random.choice(st.session_state.pool)
        st.image(scelta, caption="Immagine selezionata")
        st.session_state.pool.remove(scelta)
    else:
        st.warning("Hai esaurito le immagini!")

if st.button("Reset pool"):
    immagini = [os.path.join(IMAGES_FOLDER, f) for f in os.listdir(IMAGES_FOLDER) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
    st.session_state.pool = immagini.copy()
    st.success("Pool resettato!")
