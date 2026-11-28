# === Stage 71: Add a seed-demo-data helper with deterministic sample data ===
# Project: MealPrepBox
def seed_demo_data():
    """Populate MealPrepBox with deterministic sample data."""
    if not hasattr(MealPrepBox, "_demo_seeded"):
        MealPrepBox._demo_batches = {}
        MealPrepBox._demo_containers = {}
        MealPrepBox._demo_freezer = {}
        MealPrepBox._demo_reheating = {}
        MealPrepBox._demo_seeded = True

    MealPrepBox._demo_batches["bbq_chicken"] = {
        "name": "BBQ Chicken",
        "yield_per_batch": 4,
        "prep_minutes": 25,
        "cook_minutes": 40,
        "tags": ["protein", "dinner"],
    }
    MealPrepBox._demo_batches["veggie_bowl"] = {
        "name": "Veggie Power Bowl",
        "yield_per_batch": 3,
        "prep_minutes": 15,
        "cook_minutes": 20,
        "tags": ["vegan", "lunch"],
    }
    MealPrepBox._demo_containers["bbq_chicken"] = {
        "serving_size": 500,
        "max_servings": 6,
        "freezer_safe": True,
        "freezer_days": 5,
    }
    MealPrepBox._demo_containers["veggie_bowl"] = {
        "serving_size": 400,
        "max_servings": 4,
        "freezer_safe": True,
        "freezer_days": 6,
    }
    MealPrepBox._demo_freezer["bbq_chicken"] = 2
    MealPrepBox._demo_freezer["veggie_bowl"] = 1
    MealPrepBox._demo_reheating["bbq_chicken"] = {
        "oven_temp": 180,
        "oven_minutes": 15,
        "microwave_minutes": 2,
        "notes": "Cover with foil to retain moisture.",
    }
    MealPrepBox._demo_reheating["veggie_bowl"] = {
        "oven_temp": 170,
        "oven_minutes": 12,
        "microwave_minutes": 1,
        "notes": "Add a splash of water before heating.",
    }
