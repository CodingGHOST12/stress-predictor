
import streamlit as st
import pickle
import pandas as pd

st.title("🎓 Student Stress Predictor")

model = pickle.load(open("student_stress_model.pkl", "rb"))
features = model.feature_names_in_

sleep = st.slider("Sleep Quality (1-5)", 1, 5, 3)
headache = st.slider("Headaches/week", 0, 7, 2)
academic = st.slider("Academic (1-10)", 1, 10, 5)
study = st.slider("Study Load (1-10)", 1, 10, 5)
activity = st.slider("Activities/week", 0, 7, 2)

if st.button("Predict"):
    data = pd.DataFrame({
        features[0]: [sleep], features[1]: [headache], 
        features[2]: [academic], features[3]: [study], 
        features[4]: [activity]
    })
    pred = model.predict(data)[0]
    
    if pred <= 1:
        st.success(f"😊 Stress Level: {pred} (Low)")
    elif pred <= 3:
        st.warning(f"😐 Stress Level: {pred} (Moderate)")
    else:
        st.error(f"😰 Stress Level: {pred} (High)")
