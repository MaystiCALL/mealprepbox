# === Stage 70: Add a clear-state command protected by a confirmation flag ===
# Project: MealPrepBox
def clear_state():
    global _containers, _batches, _freezer, _confirm_clear
    if not _confirm_clear:
        print("Type 'yes' to confirm clearing all meal prep data.")
        _confirm_clear = input().strip().lower() == "yes"
    if _confirm_clear:
        _containers = []
        _batches = []
        _freezer = []
        print("All meal prep data has been cleared.")
        _confirm_clear = False
