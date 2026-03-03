from fastapi import FastAPI
import random

from core_engine.health_index import calculate_health
from risk_engine.monte_carlo import simulate_failure
from fleet.fleet_manager import rank_motors
from optimization.economic_optimizer import optimize_rpm

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Digital Twin Running"}

@app.get("/machine")
def machine_data():

    temperature = round(random.uniform(50, 80), 2)
    vibration = round(random.uniform(0.5, 2.0), 2)
    current = round(random.uniform(10, 20), 2)

    health = calculate_health(temperature, vibration, current)
    failure_probability = simulate_failure(temperature, vibration)
    rpm = optimize_rpm(vibration)

    return {
        "temperature": temperature,
        "vibration": vibration,
        "current": current,
        "health": health,
        "failure_probability": failure_probability,
        "recommended_rpm": rpm
    }