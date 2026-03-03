import random

def rank_motors():

    motors = []

    for i in range(1, 101):
        health = random.uniform(40, 100)
        motors.append({"motor_id": i, "health": health})

    motors.sort(key=lambda x: x["health"])

    return motors[:10]