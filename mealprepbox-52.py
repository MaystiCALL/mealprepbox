# === Stage 52: Add clearer docstrings for public helper functions ===
# Project: MealPrepBox
def summarize_batch(batch):
    """Summarize a batch with its containers, servings, and storage status."""
    container_count = sum(1 for c in batch.get("containers", []) if c.get("filled", False))
    total_servings = sum(c.get("servings", 0) for c in batch.get("containers", []))
    frozen = any(c.get("frozen", False) for c in batch.get("containers", []))
    return {
        "name": batch.get("name", "Batch"),
        "recipe": batch.get("recipe", ""),
        "containers": container_count,
        "total_servings": total_servings,
        "frozen_containers": sum(1 for c in batch.get("containers", []) if c.get("frozen", False)),
        "has_reheat_notes": any(c.get("reheat_note") for c in batch.get("containers", [])),
    }


def estimate_freezer_space(freezer):
    """Estimate how much freezer shelf space the current inventory requires."""
    total_volume = sum(
        c.get("volume_ml", 0) for c in freezer.get("items", []) if c.get("frozen", False)
    )
    return {
        "items": len(freezer.get("items", [])),
        "frozen_items": sum(1 for c in freezer.get("items", []) if c.get("frozen", False)),
        "total_volume_ml": total_volume,
    }


def suggest_reheat(note, method):
    """Return a clear reheating suggestion based on a note and heating method."""
    if not note:
        return "No reheating instructions were provided."
    if method == "microwave":
        return "Microwave on high for 2 to 3 minutes, stirring halfway."
    if method == "stovetop":
        return "Reheat over medium heat, stirring frequently until hot."
    if method == "oven":
        return "Bake at 180 degrees Celsius for 15 to 20 minutes."
    return "Reheat using the selected method until the food is hot throughout."
