# === Stage 62: Add simple scoring or priority recommendation logic ===
# Project: MealPrepBox
def recommend_first(items):
    score = {}
    for i, name in enumerate(items):
        score[name] = -i
    return sorted(score, key=score.get)

def suggest_meals(batches, freezer, containers):
    available = list(batches) + list(freezer)
    if not containers:
        return available
    return recommend_first([b for b in available if b in containers])

def top_items(items, limit=3):
    return recommend_first(items)[:limit]
