import numpy as np

def estimate_rul(temp, vibration, current):
    simulations = []

    for _ in range(500):
        degradation = (
            temp * np.random.uniform(0.01, 0.03)
            + vibration * np.random.uniform(0.5, 1.5)
            + current * np.random.uniform(0.02, 0.04)
        )

        rul = max(0, 100 - degradation)
        simulations.append(rul)

    return np.mean(simulations)