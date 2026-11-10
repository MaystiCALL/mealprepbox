# === Stage 43: Add CSV import for the primary record type ===
# Project: MealPrepBox
def csv_import_meals(path):
    """Import meals from a CSV file with columns: name, servings, per_serving_calories."""
    meals = []
    with open(path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"].strip()
            servings = int(row["servings"])
            calories = float(row["per_serving_calories"])
            meals.append(Meal(name=name, servings=servings, calories_per_serving=calories))
    return meals
