import streamlit as st
import pandas as pd
import pickle

# Load model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("✈️ Passenger Satisfaction Predictor")

# Input widgets
wifi = st.slider("Inflight WiFi Score (1-5)", 1, 5, 3)
delay = st.number_input("Total Delay (minutes)", 0, 500, 30)
travel_class = st.selectbox("Class", ["Economy", "Business", "Eco Plus"])  # Added Eco Plus
flight_distance = st.slider("Flight Distance (miles)", 0, 5000, 1000)  # New input
is_loyal = st.checkbox("Loyal Customer?", True)  # New input

if st.button("Predict"):
    # Create DataFrame with ALL original features
    input_data = pd.DataFrame({
        'WiFi_Score': [wifi],
        'Total_Delay': [delay],
        'Flight Distance': [flight_distance],
        'Class_Business': [1 if travel_class == "Business" else 0],
        'Class_Eco': [1 if travel_class == "Economy" else 0],
        'Class_Eco Plus': [1 if travel_class == "Eco Plus" else 0],
        'Customer Type_Loyal Customer': [1 if is_loyal else 0],
        'Customer Type_disloyal Customer': [0 if is_loyal else 1]
    })
    
    # Ensure column order matches training
    input_data = input_data[model.get_booster().feature_names]
    
    # Predict
    prob = model.predict_proba(input_data)[0][1]
    st.metric("Satisfaction Probability", f"{prob:.0%}")
