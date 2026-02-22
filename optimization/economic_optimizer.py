class EconomicOptimizer:
    @staticmethod
    def recommend_action(health, risk):
        if risk > 0.6:
            return "Immediate Maintenance"
        elif health < 50:
            return "Schedule Maintenance"
        else:
            return "Normal Operation"