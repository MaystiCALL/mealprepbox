# === Stage 20: Add duplicate detection for newly created records ===
# Project: MealPrepBox
def check_duplicate(new_record, all_records):
    """Return True if a record with the same name+size already exists."""
    for r in all_records:
        if r.get("name") == new_record.get("name") and r.get("size") == new_record.get("size"):
            return True
    return False
