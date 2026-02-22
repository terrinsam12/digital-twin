import random

class DigitalTwinService:

    def get_machine_state(self):
        temperature = random.uniform(40, 90)
        vibration = random.uniform(0.1, 2.5)
        current = random.uniform(5, 20)

        health = max(0, 100 - (temperature * 0.3 + vibration * 10 + current * 0.5))
        risk = 1 - (health / 100)

        if risk < 0.3:
            recommendation = "Normal Operation"
        elif risk < 0.6:
            recommendation = "Schedule Maintenance"
        else:
            recommendation = "High Failure Risk"

        return {
            "temperature": round(temperature, 2),
            "vibration": round(vibration, 2),
            "current": round(current, 2),
            "health": round(health, 2),
            "risk": round(risk, 2),
            "recommendation": recommendation
        }

service = DigitalTwinService()