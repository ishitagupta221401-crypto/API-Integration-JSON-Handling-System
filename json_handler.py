import json
import os

def save_to_json(data, filename):
    """Saves dictionary/list data to a JSON file in output folder"""
    try:
        os.makedirs("output", exist_ok=True)
        filepath = f"output/{filename}"
        with open(filepath, "w") as f:
            json.dump(data, f, indent=4)
        print(f"[SAVED] Data saved to {filepath}")
    except Exception as e:
        print(f"[ERROR] Could not save JSON: {e}")

def load_from_json(filename):
    """Loads and returns data from a JSON file"""
    try:
        with open(f"output/{filename}", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
        return None
    except Exception as e:
        print(f"[ERROR] Could not load JSON: {e}")
        return None