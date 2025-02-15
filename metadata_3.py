import os
import subprocess
import pandas as pd

# Directories to scan
directories = [
    "/home/roomal/Documents/School/Syllabi",
    "/home/roomal/Documents/School/Warehouse"
]

# Output CSV file
output_csv = "/home/roomal/Documents/School/all_files_metadata.csv"

# File extensions to exclude
excluded_extensions = {".md", ".csv", ".jpg", ".png"}

# Function to extract metadata
def extract_metadata(file_path):
    try:
        result = subprocess.run(
            ["exiftool", "-csv", file_path],
            capture_output=True,
            text=True
        )
        if result.returncode == 0 and result.stdout:
            return result.stdout.strip().split("\n")[1:]  # Skip header row
        else:
            return []
    except Exception as e:
        return [f"Error extracting metadata: {str(e)}"]

# Collect metadata from all valid files
metadata_list = []
for directory in directories:
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if os.path.splitext(file)[1].lower() not in excluded_extensions:
                metadata_list.extend(extract_metadata(file_path))

# Save to CSV
if metadata_list:
    with open(output_csv, "w", encoding="utf-8") as f:
        f.write("\n".join(metadata_list))

print(f"Metadata extraction completed. Saved to {output_csv}")
