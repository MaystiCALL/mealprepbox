# === Stage 14: Add file load support with fallback demo data ===
# Project: MealPrepBox
def load_from_file(filepath):
    """Load meal plan from JSON file with fallback to demo data."""
    try:
        import json
        with open(filepath, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {"meals": [], "batches": [], "containers": [], "freezer": []}
