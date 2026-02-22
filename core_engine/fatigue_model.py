class FatigueModel:
    @staticmethod
    def estimate(temperature):
        return (temperature - 50) * 0.02