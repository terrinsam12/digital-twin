import math

class WeibullModel:
    @staticmethod
    def failure_probability(age, beta=2, eta=100):
        return 1 - math.exp(-(age / eta) ** beta)