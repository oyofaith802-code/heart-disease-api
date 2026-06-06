import streamlit as st
import requests

st.title("❤️ Heart Disease Prediction App")

url = "https://heart-disease-api-e3dw.onrender.com/predict"

age = st.number_input("Age", 1, 120, 50)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])

chest_pain_type = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
resting_bp = st.number_input("Resting Blood Pressure", 50, 250, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)

fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1])
rest_ecg = st.selectbox("Rest ECG", [0, 1, 2])

max_hr = st.number_input("Max Heart Rate", 60, 220, 150)
exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])

oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)

slope = st.selectbox("Slope", [0, 1, 2])
vessels = st.selectbox("Vessels", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia", [0, 1, 2])

if st.button("Predict"):
    data = {
        "age": age,
        "sex": sex,
        "chest_pain_type": chest_pain_type,
        "resting_blood_pressure": resting_bp,
        "cholestoral": chol,
        "fasting_blood_sugar": fasting_bs,
        "rest_ecg": rest_ecg,
        "max_heart_rate": max_hr,
        "exercise_induced_angina": exercise_angina,
        "oldpeak": oldpeak,
        "slope": slope,
        "vessels": vessels,
        "thalassemia": thal
    }

    res = requests.post(url, json=data)
    result = res.json()

    st.subheader("Result")
    st.write(result)