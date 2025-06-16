import os
import json
import re
import pandas as pd
from ocr.ocr_processor import extract_text
from llm.gemini_prompt import extract_fields_with_gemini
from utils.field_mapper import get_example_schema
from utils.exporter import export_to_excel


def process_bulk(folder_path, doc_type):
    all_data = []
    files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg", ".jpeg", ".png", ".pdf"))]

    schema_example = get_example_schema(doc_type)

    for filename in files:
        image_path = os.path.join(folder_path, filename)
        print(f"📄 Processing: {filename}")
        try:
            text = extract_text(image_path)
            result_json = extract_fields_with_gemini(text, doc_type, schema_example)

            if isinstance(result_json, str):
                # Fix JSON-like strings to be Python-evaluable
                fixed_json = (
                    result_json
                    .replace('true', 'True')
                    .replace('false', 'False')
                    .replace('null', 'None')
                )
                try:
                    parsed_data = eval(fixed_json)
                except Exception as eval_error:
                    print(f"❌ Eval failed on {filename}: {eval_error}")
                    continue
            else:
                parsed_data = result_json

            parsed_data["filename"] = filename
            all_data.append(parsed_data)
        except Exception as e:
            print(f"❌ Failed on {filename}: {e}")

    export_to_excel(all_data,doc_type)
