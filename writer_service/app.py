import time
from writer_service.producer import create_producer, delivery_report
from shared.schema_loader import load_schema
from shared.avro_utils import serialize_avro

schema = load_schema("schemas/user.avsc")

producer = create_producer()

while True:
    user = {
        "user_id": "u123",
        "name":"Wamiqa",
        "age": 21,
        "email": None,
        "created_at": int(time.time())
    }

    avro_bytes = serialize_avro(user, schema)

    producer.produce(
        topic="user-topic",
        value = avro_bytes,
        callback= delivery_report
    )

    producer.flush()
    print("Event sent!")
    time.sleep(2)
