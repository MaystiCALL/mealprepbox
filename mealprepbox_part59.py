# === Stage 59: Add bulk delete behavior guarded by a confirmation flag ===
# Project: MealPrepBox
def delete_meals(meals, confirm):
    if not confirm:
        return meals
    kept = []
    for meal in meals:
        if not meal.get('deleted'):
            kept.append(meal)
    return kept

def bulk_delete(meals, meal_ids, confirm):
    if not confirm:
        return meals
    ids = set(meal_ids)
    kept = []
    for meal in meals:
        if meal.get('id') in ids:
            meal['deleted'] = True
        else:
            kept.append(meal)
    return kept

def finalize_deletions(meals):
    remaining = []
    for meal in meals:
        if not meal.get('deleted'):
            remaining.append(meal)
    return remaining
