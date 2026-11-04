# === Stage 39: Add a repair function for simple data integrity issues ===
# Project: MealPrepBox
def repair_data(db):
    if isinstance(db, dict):
        if "batches" not in db:
            db["batches"] = []
        if "containers" not in db:
            db["containers"] = []
        if "freezer" not in db:
            db["freezer"] = []
        for batch in db.get("batches", []):
            if not isinstance(batch, dict):
                db["batches"].remove(batch)
        for container in db.get("containers", []):
            if not isinstance(container, dict):
                db["containers"].remove(container)
        for item in db.get("freezer", []):
            if not isinstance(item, dict):
                db["freezer"].remove(item)
        if "reheat_notes" not in db:
            db["reheat_notes"] = {}
        for key, value in db.get("reheat_notes", {}).items():
            if not isinstance(value, str):
                db["reheat_notes"][key] = "Reheat at 350F for 20 minutes."
    return db
