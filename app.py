import streamlit as st

st.title("Crop Recommendation System")

n = st.number_input("Nitrogen")
p = st.number_input("Phosphorus")
k = st.number_input("Potassium")

if st.button("Predict"):
    st.success("Recommended Crop: Rice")
