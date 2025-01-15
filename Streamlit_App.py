import streamlit as st
import pandas as pd
import numpy as np
import joblib

joblib.load('model.joblib')

st.title("Predictive Demand Forecasting for Manufacturing")
st.subheader("Model Details")
st.text(f"Model Type: {type(model).__name__}")
st.text(f"Number of Estimators: {model.n_estimators}")
st.text(f"Feature Importance:")
st.write(pd.DataFrame({'Feature': features, 'Importance': model.feature_importances_}).sort_values(by='Importance', ascending=False))

price = st.number_input("Enter Price (GHS):", min_value=50.0, max_value=500.0, value=100.0)
discount = st.slider("Discount Percentage:", min_value=0.0, max_value=0.3, value=0.1, step=0.01)
economic_index = st.slider("Economic Index:", min_value=80.0, max_value=120.0, value=100.0, step=0.1)
advertising_spend = st.number_input("Advertising Spend (GHS):", min_value=500.0, max_value=5000.0, value=2000.0)
competitor_price = st.number_input("Competitor Price (GHS):", min_value=50.0, max_value=500.0, value=120.0)
stock_levels = st.number_input("Stock Levels:", min_value=100, max_value=2000, value=500)

if st.button("Predict Demand"):
    input_data = np.array([[price, discount, economic_index, advertising_spend, competitor_price, stock_levels]])
    prediction = loaded_model.predict(input_data)
    st.success(f"Predicted Demand: {prediction[0]:.2f} units")



