import io
from fastavro import schemaless_reader, schemaless_writer

def serialize_avro(data: dict, schema)-> bytes:
    bytes_writer = io.BytesIO()
    schemaless_writer(bytes_writer, schema, data)
    return bytes_writer.getvalue()

def deserialize_avro(data: bytes, schema) -> dict:
    bytes_reader = io.BytesIO(data)
    return schemaless_reader(bytes_reader, schema)