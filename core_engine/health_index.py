def calculate_health(temp, vibration, current):

    health = 100

    health -= temp * 0.2
    health -= vibration * 25
    health -= current * 0.3

    return max(round(health, 2), 0)