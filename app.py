import streamlit as st
import os
from main import process_document
from bulk_processor import process_bulk

# Streamlit UI
st.title("📄 Document Parser with Gemini AI")

# Upload section
upload_option = st.radio("Choose mode:", ("Single Document", "Bulk Folder"))

doc_type = st.selectbox("Select document type", [
    "birth_certificate",
    "passport",
    "police_clearance",
    "letter_of_application",
    "voter_id"
])

if upload_option == "Single Document":
    uploaded_file = st.file_uploader("Upload a document (image or PDF)", type=["jpg", "jpeg", "png", "pdf"])

    if uploaded_file:
        # Save uploaded file to a temp folder
        os.makedirs("temp", exist_ok=True)
        file_path = os.path.join("temp", uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        if st.button("Process Document"):
            process_document(file_path, doc_type)
            st.success("✅ Extraction complete. Check output/result.json")

else:
    folder_path = st.text_input("Enter folder path containing documents (images or PDFs)")
    if st.button("Process Folder"):
        if os.path.exists(folder_path):
            process_bulk(folder_path, doc_type)
            st.success("✅ Bulk processing complete. Check output/results.xlsx")
        else:
            st.error("❌ Folder path not found. Please enter a valid path.")
