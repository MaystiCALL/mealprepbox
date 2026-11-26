# === Stage 69: Add a reset-demo-data command for manual testing ===
# Project: MealPrepBox
def reset_demo_data(db):
    db.execute("DELETE FROM containers")
    db.execute("DELETE FROM batches")
    db.execute("DELETE FROM freezer_inventory")
    db.execute("DELETE FROM recipes")
    demo_recipes = [
        ("Chicken Basil Bowl", "batch_001"),
        ("Beef Stir Fry", "batch_002"),
        ("Veggie Curry", "batch_003"),
    ]
    demo_containers = []
    for recipe_name, batch_id in demo_recipes:
        demo_containers.append((recipe_name, batch_id, "cooked", "reheat at 350F for 15 min"))
    db.executemany("INSERT INTO containers (recipe, batch_id, status, reheating_note) VALUES (?, ?, ?, ?)", demo_containers)
    demo_freezer = [("batch_002", 3, "2024-06-01"), ("batch_003", 2, "2024-06-02")]
    db.executemany("INSERT INTO freezer_inventory (batch_id, quantity, frozen_date) VALUES (?, ?, ?)", demo_freezer)
    db.commit()
