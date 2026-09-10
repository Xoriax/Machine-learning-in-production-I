import streamlit as st
import joblib

#chargement du model depuis regression.joblib
model = joblib.load("regression.joblib")

#mes 3 champs de form demande
size = st.number_input("Taille (m²)")
nbr_rooms = st.number_input("Nombre de chambres")
garden = st.number_input("Jardin (0 = non, 1 = oui)")

#recup et transmition au model via predict
prediction = model.predict([[size, nbr_rooms, garden]])
#affichage avec streamlit
st.write(prediction)