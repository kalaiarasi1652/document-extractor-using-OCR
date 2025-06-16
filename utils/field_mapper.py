import json

def load_schema(doc_type):
    with open('config/schema.json', 'r') as f:
        schemas = json.load(f)
    return schemas.get(doc_type, {})

def get_example_schema(doc_type):
    schema = load_schema(doc_type)
    example = {standard: "..." for standard in schema}
    return example
