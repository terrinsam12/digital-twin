import random
import time
import boto3

cloudwatch = boto3.client("cloudwatch", region_name="us-east-1")

def generate_motor_data():
    temp = random.uniform(40, 120)
    vibration = random.uniform(0.2, 2.5)
    current = random.uniform(5, 25)

    return temp, vibration, current

def send_to_cloudwatch(temp, vibration, current):
    cloudwatch.put_metric_data(
        Namespace="DigitalTwin/Motor",
        MetricData=[
            {"MetricName": "Temperature", "Value": temp, "Unit": "None"},
            {"MetricName": "Vibration", "Value": vibration, "Unit": "None"},
            {"MetricName": "Current", "Value": current, "Unit": "None"},
        ],
    )

while True:
    t, v, c = generate_motor_data()
    send_to_cloudwatch(t, v, c)
    print("Sent:", t, v, c)
    time.sleep(5)