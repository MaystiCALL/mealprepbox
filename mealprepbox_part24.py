# === Stage 24: Add grouped summaries by category or status ===
# Project: MealPrepBox
def summarize_batches(batches):
    """Return a compact grouped summary of batches by category or status."""
    groups = {}
    for b in batches:
        key = b.get("category") or b.get("status", "other")
        groups.setdefault(key, []).append(b)
    return {k: sorted(v, key=lambda x: x.get("date", "")) for k, v in groups.items()}
