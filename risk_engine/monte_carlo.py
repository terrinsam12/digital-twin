import random

def simulate_failure(temp, vibration):

    failures = 0
    simulations = 1000

    for _ in range(simulations):
        temp_variation = temp + random.uniform(-2, 2)
        vib_variation = vibration + random.uniform(-0.2, 0.2)

        risk_score = temp_variation * 0.3 + vib_variation * 40

        if risk_score > 50:
            failures += 1

    return round(failures / simulations, 3)