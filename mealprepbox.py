# === Stage 1: Create the base application structure, in-memory state, and a small demo dataset ===
# Project: MealPrepBox
import json

# In-memory state for the MealPrepBox planner
state = {
    "batches": [
        {"name": "Chicken Stir-Fry", "date": "2024-01-15", "containers": 6, "freezer": False},
        {"name": "Vegetable Soup", "date": "2024-01-16", "containers": 4, "freezer": True}
    ],
    "containers": [
        {"id": "C001", "batch": "Chicken Stir-Fry", "status": "eaten"},
        {"id": "C002", "batch": "Chicken Stir-Fry", "status": "leftover"},
        {"id": "C003", "batch": "Vegetable Soup", "status": "leftover"},
        {"id": "C004", "batch": "Vegetable Soup", "status": "leftover"},
        {"id": "C005", "batch": "Vegetable Soup", "status": "frozen"}
    ],
    "freezer_inventory": [
        {"item": "Vegetable Soup", "date_frozen": "2024-01-16", "quantity": 3}
    ],
    "reheating_notes": [
        {"batch": "Chicken Stir-Fry", "method": "Microwave 3 min", "notes": "Let stand 1 min before eating"},
        {"batch": "Vegetable Soup", "method": "Microwave 5 min", "notes": "Stir halfway through"}
    ]
}

# Demo dataset: add a new batch entry
new_batch = {
    "name": "Beef Tacos",
    "date": "2024-01-17",
    "containers": 8,
    "freezer": False
}
state["batches"].append(new_batch)

# Print the current state for verification
print("MealPrepBox State:")
print(json.dumps(state, indent=2))
