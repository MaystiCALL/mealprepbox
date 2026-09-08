# === Stage 8: Add filtering by status, category, owner, or tag ===
# Project: MealPrepBox
def filter_meals(meals, filters):
    """Filter meals by status, category, owner, tag (any subset of filters)."""
    if not filters:
        return list(meals)

    result = []
    for meal in meals:
        match = True
        for key, value in filters.items():
            if key == "status":
                if meal.get("status") != value:
                    match = False
                    break
            elif key == "category":
                if meal.get("category") != value:
                    match = False
                    break
            elif key == "owner":
                if meal.get("owner") != value:
                    match = False
                    break
            elif key == "tag":
                if value not in meal.get("tags", []):
                    match = False
                    break
            else:
                if meal.get(key) != value:
                    match = False
                    break
        if match:
            result.append(meal)
    return result
