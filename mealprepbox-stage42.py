# === Stage 42: Add CSV export without external dependencies ===
# Project: MealPrepBox
def export_to_csv(planner):
    rows = [["name", "batch_size", "freezer_count", "reheat_temp", "reheat_time", "notes"]]
    for meal in planner.meals:
        batch = planner.get_batch(meal.name) or {}
        rows.append([
            meal.name,
            batch.get("batch_size", ""),
            meal.freezer_count,
            meal.reheat_temp,
            meal.reheat_time,
            meal.notes,
        ])
    import csv
    filename = "meal_prep_export.csv"
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return filename
