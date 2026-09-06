# === Stage 6: Implement delete operations with a confirmation flag argument ===
# Project: MealPrepBox
def delete_entry(key, confirm=False):
    """
    Safely remove an entry from the meal database.
    
    Args:
        key (str): The identifier of the entry to delete (e.g., meal name).
        confirm (bool): If True, prompts user for confirmation before deleting.
    
    Returns:
        bool: True if the entry was deleted, False otherwise.
    """
    if key not in meal_db:
        print(f"Entry '{key}' not found.")
        return False
    
    if confirm:
        user_input = input(f"Are you sure you want to delete '{key}'? (y/n): ")
        if user_input.lower() != 'y':
            print("Deletion cancelled.")
            return False
    
    del meal_db[key]
    print(f"Entry '{key}' successfully deleted.")
    return True
