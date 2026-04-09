from confluent_kafka import Consumer
import os

def create_consumer():
    return Consumer({
        'bootstrap.servers': 'localhost:9092',
        'group.id': 'user-consumer-group',
        'auto.offset.reset': 'earliest'
    })