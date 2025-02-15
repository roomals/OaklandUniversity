import os
import subprocess
import csv

# Directories to scan
source_dirs = [
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY2410 - Exam-2",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY3180-30540",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY3390-44348",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY-2410",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY-2410 (1)",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY-3030",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY-3030-1",
    "/home/roomal/Documents/School/Warehouse/Consolidated/PSY_3390_-_Emotion_44348"
]

# Output CSV file
output_csv = "/home/roomal/Documents/School/Warehouse/Consolidated/all_files_metadata.csv"

# Command to run ExifTool
exiftool_cmd = ["exiftool", "-csv", "-r"] + source_dirs

try:
    # Run ExifTool and capture output with proper encoding handling
    result = subprocess.run(exiftool_cmd, capture_output=True, text=True, errors="replace")

    # Decode safely using UTF-8, replacing problematic characters
    metadata = result.stdout.encode("utf-8", "replace").decode("utf-8")

    # Save metadata to CSV
    with open(output_csv, "w", newline="", encoding="utf-8") as f:
        f.write(metadata)

    print(f"\n✅ Metadata extracted successfully! Saved to: {output_csv}")

except Exception as e:
    print(f"❌ Error extracting metadata: {e}")