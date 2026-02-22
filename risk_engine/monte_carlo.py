import random

class MonteCarlo:
    @staticmethod
    def simulate(probability, trials=1000):
        failures = sum(random.random() < probability for _ in range(trials))
        return failures / trials