import json

class MQTTListener:
    def __init__(self):
        self.latest_data = {}

    def simulate_receive(self):
        """
        Simulated hardware data (replace with real MQTT later)
        """
        self.latest_data = {
            "temperature": 75,
            "vibration": 0.35,
            "pressure": 101.5,
            "humidity": 60
        }
        return self.latest_data