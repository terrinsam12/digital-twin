from fastapi import FastAPI
import random

from core_engine.health_index import calculate_health
from risk_engine.monte_carlo import simulate_failure
from fleet.fleet_manager import rank_motors
from optimization.economic_optimizer import optimize_rpm

app = FastAPI()

# Home check
@app.get("/")
def home():
    return {"message": "Digital Twin Running Successfully"}

# Single machine monitoring
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

# Fleet monitoring (100 motors)
@app.get("/fleet")
def fleet_monitor():

    motors = []

    for i in range(100):

        temp = random.uniform(50, 90)
        vib = random.uniform(0.3, 2.5)
        cur = random.uniform(8, 22)

        health = calculate_health(temp, vib, cur)
        failure = simulate_failure(temp, vib)

        motors.append({
            "motor_id": i + 1,
            "temperature": temp,
            "vibration": vib,
            "current": cur,
            "health": health,
            "failure_probability": failure
        })

    ranked = rank_motors(motors)

    return ranked