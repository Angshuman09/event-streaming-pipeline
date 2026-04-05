import json
from fastavro import parse_schema

def load_schema(schema_path: str):
    with open(schema_path, "r") as f:
        schema = json.load(f)
        
    return parse_schema(schema)