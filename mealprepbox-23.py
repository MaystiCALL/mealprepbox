# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: MealPrepBox
def add_tag(recipe, tag):
    if tag not in recipe.tags:
        recipe.tags.append(tag)
    return recipe

def remove_tag(recipe, tag):
    if tag in recipe.tags:
        recipe.tags.remove(tag)
    return recipe

def summary_by_tag(all_recipes, tag):
    return [r for r in all_recipes if tag in r.tags]
