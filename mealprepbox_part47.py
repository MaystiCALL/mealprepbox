# === Stage 47: Add a demo scenario that exercises the main workflow ===
# Project: MealPrepBox
def demo_scenario():
    inventory = MealPrepBox()
    inventory.add_recipe("Chicken Stir Fry", portions_per_batch=4,
                         reheating_note="Microwave 2 min on defrost, then 3 min high.")
    inventory.add_recipe("Vegetable Curry", portions_per_batch=6,
                         reheating_note="Stir well; reheat gently to avoid splitting.")
    batch = inventory.create_batch("Chicken Stir Fry", 2)
    inventory.add_container(batch, "Chicken Stir Fry", "20250110", "20250113")
    inventory.add_container(batch, "Chicken Stir Fry", "20250111", "20250114")
    inventory.add_container(batch, "Chicken Stir Fry", "20250112", "20250115")
    inventory.freeze_container(batch, "Chicken Stir Fry", "20250113", "20250125",
                               "Reheat in microwave 3-4 min before serving.")
    inventory.add_recipe("Fish Tacos", portions_per_batch=3,
                         reheating_note="Air fry at 180C for 8 minutes.")
    batch2 = inventory.create_batch("Fish Tacos", 1)
    inventory.add_container(batch2, "Fish Tacos", "20250110", "20250112")
    print("Batches:", sorted(inventory.list_batches()))
    print("Freezer items:", sorted(inventory.list_freezer_items()))
    print("Available meals:", sorted(inventory.list_available_meals()))
    print("Reheating note for Chicken Stir Fry:",
          inventory.get_recipe("Chicken Stir Fry").reheating_note)
    print("Total recipes:", inventory.count_recipes())
    print("Total containers:", inventory.count_containers())
