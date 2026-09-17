# === Stage 26: Add weekly summary calculations ===
# Project: MealPrepBox
def weekly_summary(meals, weeks):
    """Compute per-week calorie and protein totals from a list of meal dicts
    and a list of week numbers (1-indexed)."""
    if not meals or not weeks:
        return []
    weeks_set = set(weeks)
    total = {
        "total_calories": 0,
        "total_protein": 0,
        "total_carbs": 0,
        "total_fat": 0,
    }
    weekly = {}
    for m in meals:
        if m["week"] not in weeks_set:
            continue
        if m["week"] not in weekly:
            weekly[m["week"]] = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
        weekly[m["week"]]["calories"] += m["calories"]
        weekly[m["week"]]["protein"] += m["protein"]
        weekly[m["week"]]["carbs"] += m["carbs"]
        weekly[m["week"]]["fat"] += m["fat"]
        total["total_calories"] += m["calories"]
        total["total_protein"] += m["protein"]
        total["total_carbs"] += m["carbs"]
        total["total_fat"] += m["fat"]
    sorted_weeks = sorted(weekly.keys())
    result = [
        {"week": w, "calories": weekly[w]["calories"],
         "protein": weekly[w]["protein"], "carbs": weekly[w]["carbs"],
         "fat": weekly[w]["fat"]}
        for w in sorted_weeks
    ]
    result.append(total)
    return result
