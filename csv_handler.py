import csv
import os

def save_to_csv(data, filename, fieldnames):
    """Saves list of dicts to a CSV file in output folder"""
    try:
        os.makedirs("output", exist_ok=True)
        filepath = f"output/{filename}"
        with open(filepath, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"[SAVED] CSV saved to {filepath}")
    except Exception as e:
        print(f"[ERROR] Could not save CSV: {e}")