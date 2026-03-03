import streamlit as st
import requests
import time

st.set_page_config(layout="wide")

st.title("Digital Twin Monitoring Dashboard")

# Layout
col1, col2, col3 = st.columns(3)
col4, col5, col6 = st.columns(3)

temp_box = col1.empty()
vib_box = col2.empty()
curr_box = col3.empty()
health_box = col4.empty()
fail_box = col5.empty()
rpm_box = col6.empty()

chart_placeholder = st.empty()

temperature_history = []
vibration_history = []
health_history = []

while True:
    data = requests.get("http://127.0.0.1:8000/machine").json()

    temp = data["temperature"]
    vib = data["vibration"]
    curr = data["current"]
    health = data["health"]
    failure = data["failure_probability"]
    rpm = data["recommended_rpm"]

    # Update metrics
    temp_box.metric("Temperature (°C)", temp)
    vib_box.metric("Vibration", vib)
    curr_box.metric("Current (A)", curr)
    health_box.metric("Health (%)", health)
    fail_box.metric("Failure Probability", failure)
    rpm_box.metric("Recommended RPM", rpm)

    # Store history
    temperature_history.append(temp)
    vibration_history.append(vib)
    health_history.append(health)

    # Keep last 50 values
    temperature_history = temperature_history[-50:]
    vibration_history = vibration_history[-50:]
    health_history = health_history[-50:]

    chart_placeholder.line_chart({
        "Temperature": temperature_history,
        "Vibration": vibration_history,
        "Health": health_history
    })

    time.sleep(2)