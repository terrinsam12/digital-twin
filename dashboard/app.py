import streamlit as st
import requests
import time

st.set_page_config(page_title="Digital Twin Dashboard", layout="wide")

st.title("Machine Digital Twin Monitoring")

API_URL = "http://127.0.0.1:8000/machine"

placeholder = st.empty()

while True:
    try:
        data = requests.get(API_URL).json()

        with placeholder.container():
            col1, col2, col3 = st.columns(3)

            col1.metric("Temperature", f"{data['temperature']:.2f} °C")
            col2.metric("Vibration", f"{data['vibration']:.2f} g")
            col3.metric("Current", f"{data['current']:.2f} A")

            st.subheader("Health Status")
            st.progress(data["health"] / 100)

            st.write("Risk Level:", data["risk"])
            st.write("Recommendation:", data["recommendation"])

        time.sleep(2)

    except:
        st.error("API not running")
        time.sleep(2)