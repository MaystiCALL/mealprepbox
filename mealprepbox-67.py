# === Stage 67: Add a function that returns key project metrics ===
# Project: MealPrepBox
def get_project_metrics(batches, containers, freezer):
    total_batches = len(batches)
    total_containers = len(containers)
    total_freezer_items = len(frozen)
    total_served = sum(b['containers_served'] for b in batches)
    total_reheated = sum(c['reheats'] for c in containers)
    total_meals = total_served * total_containers
    return {
        'total_batches': total_batches,
        'total_containers': total_containers,
        'total_freezer_items': total_freezer_items,
        'total_served': total_served,
        'total_reheated': total_reheated,
        'total_meals': total_meals,
    }
