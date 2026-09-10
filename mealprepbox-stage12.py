# === Stage 12: Add JSON import with friendly error handling for malformed data ===
# Project: MealPrepBox
import json

def load_recipe(filepath):
    """Load a recipe from a JSON file with friendly error handling."""
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        if not isinstance(data, dict) or 'name' not in data:
            raise ValueError("Recipe JSON must be a dict with a 'name' field.")
        return data
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error: Malformed JSON in '{filepath}': {e}")
    except Exception as e:
        print(f"Error: Unexpected issue loading '{filepath}': {e}")
        return None

# Example usage:
# recipe = load_recipe("recipes/meal_prep_box.json")
# if recipe:
#     print(f"{recipe['name']}: {recipe.get('prep_time', 'N/A')} minutes")
