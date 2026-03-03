import numpy as np
from sklearn.ensemble import RandomForestClassifier

X = []
y = []

for _ in range(1000):
    temp = np.random.uniform(40, 120)
    vibration = np.random.uniform(0.2, 2.5)
    current = np.random.uniform(5, 25)

    failure = 1 if (temp > 95 or vibration > 1.8 or current > 20) else 0

    X.append([temp, vibration, current])
    y.append(failure)

model = RandomForestClassifier()
model.fit(X, y)

def predict_failure(temp, vibration, current):
    prob = model.predict_proba([[temp, vibration, current]])[0][1]
    return prob