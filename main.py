import json
import os
import argparse
from ocr.ocr_processor import extract_text
from llm.gemini_prompt import extract_fields_with_gemini
from utils.field_mapper import get_example_schema
from bulk_processor import process_bulk

def process_document(image_path, doc_type):
    print(f"📄 Processing: {image_path}")

    # Extract text from image
    text = extract_text(image_path)

    # Get schema example for prompt
    schema_example = get_example_schema(doc_type)

    # Get LLM output
    try:
        result_str = extract_fields_with_gemini(text, doc_type, schema_example)
        print(result_str)
        result_data = result_str
    except Exception as e:
        print("❌ Error parsing Gemini output:", e)
        return

    # Ensure output folder exists
    os.makedirs('output', exist_ok=True)

    # Save result
    with open('output/result.json', 'w') as f:
        json.dump(result_data, f, indent=2)

    print("✅ Extraction complete. See output/result.json")

def main():
    parser = argparse.ArgumentParser(description="Document Parser Tool")
    parser.add_argument("--folder", type=str, default="data/examples", help="Folder containing documents")
    parser.add_argument("--single", type=str, help="Path to single document (image/pdf)")
    parser.add_argument("--doc_type", type=str, required=True, help="Document type (e.g., birth_certificate, passport)")

    args = parser.parse_args()

    if args.single:
        process_document(args.single, args.doc_type)
    else:
        process_bulk(args.folder, args.doc_type)

if __name__ == "__main__":
    main()
