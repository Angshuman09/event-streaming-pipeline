from confluent_kafka import Producer
import os

def create_producer():
    return Producer({
        'bootstrap.servers': os.getenv('KAFKA_BOOTSTRAP_SERVERS', 'localhost:9092')
    })

def delivery_report(err, msg):
    if err is not None:
        print("Message delivery failed: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")
        