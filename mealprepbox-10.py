# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: MealPrepBox
def search_meals(query, meals):
    query = query.strip().lower()
    if not query:
        return meals
    results = []
    for meal in meals:
        for field in ['name', 'description', 'prep_time', 'cook_time', 'container_material', 'reheat_instructions']:
            if field in meal and query in str(meal[field]).lower():
                results.append(meal)
                break
    return results
