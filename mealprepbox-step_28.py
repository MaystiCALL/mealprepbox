# === Stage 28: Add overdue item detection based on due dates ===
# Project: MealPrepBox
def find_overdue_items(frozen_plan, due_date):
    """Return list of frozen items whose due date has passed."""
    overdue = []
    for item in frozen_plan:
        if item["due_date"] and item["due_date"] < due_date:
            overdue.append({
                "name": item["name"],
                "due_date": item["due_date"],
                "reheat_instructions": item.get("reheat_instructions", "N/A"),
                "container_type": item.get("container_type", "unknown"),
            })
    return overdue
