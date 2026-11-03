# === Stage 38: Add data integrity checks for broken references ===
# Project: MealPrepBox
def check_references(meals, containers, freezer):
    meal_ids = {m["id"] for m in meals}
    container_ids = {c["id"] for c in containers}
    freezer_ids = {f["id"] for f in freezer}

    for meal in meals:
        for ref in ("containers", "freezer"):
            for item in meal.get(ref, []):
                if ref == "containers" and item["id"] not in container_ids:
                    raise ValueError(f"Meal {meal['id']} references missing container {item['id']}")
                if ref == "freezer" and item["id"] not in freezer_ids:
                    raise ValueError(f"Meal {meal['id']} references missing freezer {item['id']}")

    for freezer_item in freezer:
        if freezer_item.get("meal_id") not in meal_ids:
            raise ValueError(f"Freezer {freezer_item['id']} references missing meal {freezer_item['meal_id']}")

    for meal in meals:
        for batch_ref in meal.get("batches", []):
            if batch_ref["id"] not in {b["id"] for b in meal.get("batches", [])}:
                raise ValueError(f"Meal {meal['id']} references missing batch {batch_ref['id']}")
