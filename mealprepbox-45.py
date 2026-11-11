# === Stage 45: Add restore from backup with validation ===
# Project: MealPrepBox
def restore_from_backup(filename, validate=True):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Backup file not found: {filename}")
    with open(filename, "r", encoding="utf-8") as f:
        data = json.load(f)
    if validate:
        if not isinstance(data, dict):
            raise ValueError("Backup data must be a JSON object")
        for key in ("batches", "containers", "freezer", "reheating_notes"):
            if key not in data:
                raise ValueError(f"Missing required key in backup: {key}")
        for batch in data["batches"]:
            if not isinstance(batch, dict) or "name" not in batch:
                raise ValueError("Each batch must be a dict with a 'name'")
        for container in data["containers"]:
            if not isinstance(container, dict) or "batch" not in container:
                raise ValueError("Each container must be a dict with a 'batch'")
        for recipe, notes in data["reheating_notes"].items():
            if not isinstance(notes, dict):
                raise ValueError("Reheating notes must be a dict")
    planner.batches = data["batches"]
    planner.containers = data["containers"]
    planner.freezer = data["freezer"]
    planner.reheating_notes = data["reheating_notes"]
    return planner
