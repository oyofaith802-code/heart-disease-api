import streamlit as st
import requests

# PAGE CONFIG
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="centered"
)

# TITLE
st.title("❤️ Heart Disease Risk Prediction App")
st.write("Enter patient details below to predict risk level.")

url = "https://heart-disease-api-e3dw.onrender.com/predict"

# INPUT UI (BETTER LAYOUT)
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 50)
    sex = st.selectbox("Sex", [0, 1])
    chest_pain_type = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    resting_bp = st.number_input("Resting Blood Pressure", 50, 250, 120)
    chol = st.number_input("Cholesterol", 100, 600, 200)
    fasting_bs = st.selectbox("Fasting Blood Sugar", [0, 1])

with col2:
    rest_ecg = st.selectbox("Rest ECG", [0, 1, 2])
    max_hr = st.number_input("Max Heart Rate", 60, 220, 150)
    exercise_angina = st.selectbox("Exercise Induced Angina", [0, 1])
    oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
    slope = st.selectbox("Slope", [0, 1, 2])
    vessels = st.selectbox("Vessels", [0, 1, 2, 3])
    thal = st.selectbox("Thalassemia", [0, 1, 2])

# BUTTON
if st.button("🔍 Predict Risk"):

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

    with st.spinner("Predicting..."):
        res = requests.post(url, json=data)

    result = res.json()

    # RESULT DISPLAY
    st.subheader("🧾 Result")

    if result["prediction"] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")