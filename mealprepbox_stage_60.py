# === Stage 60: Add saved views for frequently used filters ===
# Project: MealPrepBox
SAVE = "saved_views.json"

def save_view(name, filters):
    views = load_views()
    views[name] = filters
    with open(SAVE, "w") as f:
        json.dump(views, f)

def load_views():
    if not os.path.exists(SAVE):
        return {}
    with open(SAVE) as f:
        return json.load(f)

def list_views():
    for name in load_views():
        print(f"  - {name}")

def apply_saved_view(name):
    filters = load_views().get(name, {})
    return filters
