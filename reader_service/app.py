from reader_service.consumer import create_consumer
from shared.schema_loader import load_schema
from shared.avro_utils import deserialize_avro

schema = load_schema("schemas/user.avsc")

consumer = create_consumer()

consumer.subscribe(["user-topic"])

print("Listening for messages...\n")

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue

    if msg.error():
        print("Consumer error: ", msg.error())
        continue

    avro_bytes = msg.value()
    user_data = deserialize_avro(avro_bytes, schema)
    print("Received user data:", user_data)