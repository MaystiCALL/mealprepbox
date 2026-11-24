# === Stage 64: Add validation for relationship references ===
# Project: MealPrepBox
def validate_relationships(inventory):
    valid_meal_ids = {meal['id'] for meal in inventory.get('meals', [])}
    valid_batch_ids = {batch['id'] for batch in inventory.get('batches', [])}
    valid_container_ids = {c['id'] for c in inventory.get('containers', [])}
    valid_freezer_ids = {f['id'] for f in inventory.get('freezer_inventory', [])}
    for batch in inventory.get('batches', []):
        if batch.get('meal_id') not in valid_meal_ids:
            raise ValueError(f"Batch {batch['id']} references unknown meal_id")
        if batch.get('container_id') not in valid_container_ids:
            raise ValueError(f"Batch {batch['id']} references unknown container_id")
        for recipe in batch.get('recipes', []):
            if recipe.get('batch_id') not in valid_batch_ids:
                raise ValueError(f"Recipe {recipe['id']} references unknown batch_id")
    for freezer_item in inventory.get('freezer_inventory', []):
        if freezer_item.get('batch_id') not in valid_batch_ids:
            raise ValueError(f"Freezer item {freezer_item['id']} references unknown batch_id")
        if freezer_item.get('container_id') not in valid_container_ids:
            raise ValueError(f"Freezer item {freezer_item['id']} references unknown container_id")
    return True
