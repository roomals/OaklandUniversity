import subprocess
import csv
import os
import json

# Output CSV file name
OUTPUT_CSV = "all_files_metadata.csv"

def extract_metadata(file_path):
    """Runs ExifTool on any file and extracts metadata as a dictionary."""
    try:
        # Run exiftool and capture JSON output
        result = subprocess.run(
            ["exiftool", "-j", file_path],
            capture_output=True,
            text=True,
            check=True
        )

        # Parse JSON output
        metadata = json.loads(result.stdout)
        return metadata[0] if metadata else {}

    except subprocess.CalledProcessError as e:
        print(f"Error running exiftool on {file_path}: {e}")
        return {}

def write_metadata_to_csv(directory):
    """Extracts metadata from ALL files in a directory and writes to CSV."""
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]

    if not files:
        print("No files found in the directory.")
        return

    all_metadata = []

    for file in files:
        file_path = os.path.join(directory, file)
        metadata = extract_metadata(file_path)

        if metadata:
            all_metadata.append(metadata)
            print(f"Processed: {file}")

    if not all_metadata:
        print("No metadata extracted from any files.")
        return

    # Collect all unique keys (metadata fields)
    all_keys = set()
    for data in all_metadata:
        all_keys.update(data.keys())

    # Write to CSV
    with open(OUTPUT_CSV, mode="w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=sorted(all_keys))
        writer.writeheader()

        for data in all_metadata:
            writer.writerow(data)

    print(f"\nMetadata saved to {OUTPUT_CSV}")

if __name__ == "__main__":
    input_directory = input("Enter the directory containing files: ").strip()
    write_metadata_to_csv(input_directory)