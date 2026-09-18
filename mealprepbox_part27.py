# === Stage 27: Add monthly summary calculations ===
# Project: MealPrepBox
def monthly_summary(boxes, months):
    """Compute a compact monthly summary for meal prep boxes."""
    summary = {}
    for month in months:
        total = 0
        boxes_this_month = 0
        for box in boxes:
            if box['month'] == month:
                boxes_this_month += 1
                total += box.get('total_calories', 0)
        summary[month] = {'boxes': boxes_this_month, 'total_calories': total}
    return summary
