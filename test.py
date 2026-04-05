from shared.schema_loader import load_schema
from shared.avro_utils import serialize_avro, deserialize_avro
import time

schema = load_schema("schemas/user.avsc")
print("Loaded Avro schema:", schema)

user = {
    "user_id": "u123",
    "name": "Angshu",
    "age": 21,
    "email": None,
    "created_at": int(time.time())
}

avro_bytes = serialize_avro(user, schema)
print("Serialized Avro bytes:", avro_bytes)

decoded = deserialize_avro(avro_bytes, schema)
print("Deserialized Avro data:", decoded)