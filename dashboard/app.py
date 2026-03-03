import streamlit as st
import requests
import pandas as pd
import time

st.set_page_config(page_title="Digital Twin Dashboard", layout="wide")

API_URL = "http://127.0.0.1:8000/machine"

st.title("Digital Twin Motor Monitoring")

data_history = []

placeholder = st.empty()

while True:
    try:
        response = requests.get(API_URL)
        data = response.json()
    except:
        st.error("FastAPI server not running")
        break

    data_history.append(data)
    df = pd.DataFrame(data_history)

    with placeholder.container():

        col1, col2, col3, col4 = st.columns(4)

        col1.metric("Temperature", data["temperature"])
        col2.metric("Vibration", data["vibration"])
        col3.metric("Current", data["current"])
        col4.metric("Health", data["health"])

        col5, col6 = st.columns(2)
        col5.metric("Failure Probability", data["failure_probability"])
        col6.metric("Recommended RPM", data["recommended_rpm"])

        st.divider()

        st.subheader("Motor Trend Analysis")
        st.line_chart(df)

    time.sleep(2)