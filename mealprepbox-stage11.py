# === Stage 11: Add JSON export for the current application state ===
# Project: MealPrepBox
def export_state():
    """Export current application state as JSON."""
    import json
    state = {
        "meals": {
            meal["name"]: {
                "batches": meal["batches"],
                "containers": meal["containers"],
                "freezer_inv": meal["freezer_inv"],
                "reheat_notes": meal["reheat_notes"]
            }
            for meal in meal_list
        },
        "last_updated": datetime.now().isoformat()
    }
    return json.dumps(state, indent=2)
