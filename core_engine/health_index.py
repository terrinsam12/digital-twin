class HealthIndex:
    @staticmethod
    def compute(sensor_data):
        score = 100

        score -= abs(sensor_data["temperature"] - 70) * 0.5
        score -= sensor_data["vibration"] * 50
        score -= abs(sensor_data["pressure"] - 101) * 0.3
        score -= abs(sensor_data["humidity"] - 50) * 0.2

        return max(score, 0)