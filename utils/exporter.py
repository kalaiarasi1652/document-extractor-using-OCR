import os
import pandas as pd
from datetime import datetime

def export_to_excel(data_list, doc_type, output_dir="output"):
    # Create schema-specific subfolder
    folder_path = os.path.join(output_dir, doc_type)
    os.makedirs(folder_path, exist_ok=True)

    # Optional: add timestamp for batch versioning
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{doc_type}_results_{timestamp}.xlsx"
    output_path = os.path.join(folder_path, filename)

    df = pd.DataFrame(data_list)
    df.to_excel(output_path, index=False)
    print(f"📁 Excel exported to: {output_path}")

def export_to_csv(data_list, doc_type, output_dir="output"):
    folder_path = os.path.join(output_dir, doc_type)
    os.makedirs(folder_path, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{doc_type}_results_{timestamp}.csv"
    output_path = os.path.join(folder_path, filename)

    df = pd.DataFrame(data_list)
    df.to_csv(output_path, index=False)
    print(f"📁 CSV exported to: {output_path}")
