import google.generativeai as genai

genai.configure(api_key='AIzaSyDYqxl7r2hrNlq2UKLJ3M6dt32W_etEUoM')

def extract_fields_with_gemini(document_text, doc_type, schema_example):
    model = genai.GenerativeModel('gemini-1.5-flash')
    print(document_text)
    prompt = f"""
        You are an expert in extracting structured data from messy text.
        Document Type: {doc_type}
        Text:
        {document_text}
        Extract and map fields based on this schema example:
        {schema_example}
        extract the data based on the doc_type and the schema_example given
        Also answer:
        - Is this a scanned document? true/false
        - Confidence level for document type: high/medium/low
        and don't include json in the top 

        Respond only in JSON and add these fields below too:
        "meta": {{
             "is_scanned": true,
             "document_type_confidence": "high"
        }}
    """
    response = model.generate_content(prompt)
    response = response.text
    if response.strip().startswith("```json"):
        response = response.strip().split("```json")[1].split("```")[0].strip()
    print(response)
    return response
