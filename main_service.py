from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Digital Twin API Running"}

@app.get("/machine")
def machine_data():
    temperature = round(random.uniform(50, 80), 2)
    vibration = round(random.uniform(0.5, 2.0), 2)
    current = round(random.uniform(10, 20), 2)

    health = round(100 - (temperature * 0.3 + vibration * 20 + current * 0.2), 2)
    risk = round(1 - health / 100, 2)

    if risk > 0.7:
        recommendation = "Immediate Maintenance"
    elif risk > 0.4:
        recommendation = "Schedule Maintenance"
    else:
        recommendation = "Normal Operation"

    return {
        "temperature": temperature,
        "vibration": vibration,
        "current": current,
        "health": health,
        "risk": risk,
        "recommendation": recommendation
    }
