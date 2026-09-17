# === Stage 25: Add daily summary calculations ===
# Project: MealPrepBox
def daily_summary(batches):
    """Return a compact daily summary dict for meal prepping.

    Args:
        batches (list[dict]): each batch has keys:
            'date' (str), 'prep_time_min' (int), 'cook_time_min' (int),
            'containers' (int), 'freezer_stored' (bool), 'reheat_notes' (str)

    Returns:
        dict with keys:
            date, prep_time_total, cook_time_total, containers_total,
            freezer_count, reheat_notes, batch_count
    """
    if not batches:
        return {
            "date": None, "prep_time_total": 0, "cook_time_total": 0,
            "containers_total": 0, "freezer_count": 0, "reheat_notes": "",
            "batch_count": 0
        }
    date = batches[0]["date"]
    prep_total = sum(b["prep_time_min"] for b in batches)
    cook_total = sum(b["cook_time_min"] for b in batches)
    containers_total = sum(b["containers"] for b in batches)
    freezer_count = sum(1 for b in batches if b["freezer_stored"])
    reheat_notes = "; ".join(b["reheat_notes"] for b in batches)
    return {
        "date": date,
        "prep_time_total": prep_total,
        "cook_time_total": cook_total,
        "containers_total": containers_total,
        "freezer_count": freezer_count,
        "reheat_notes": reheat_notes,
        "batch_count": len(batches)
    }
