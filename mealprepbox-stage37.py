# === Stage 37: Add recommendations for the next useful action ===
# Project: MealPrepBox
def recommend_next_action(plan):
    """
    Suggests the next useful action based on the current meal plan state.
    """
    if not plan.get("frozen_items"):
        return "Add frozen items to your plan for future use."
    if not plan.get("containers"):
        return "Organize your containers before starting meal prep."
    if not plan.get("batches"):
        return "Define your batches to start cooking."
    if not plan.get("reheat_notes"):
        return "Add reheating instructions for each batch."
    if not plan.get("ingredients"):
        return "List your ingredients to ensure you have everything."
    return "Your plan is complete. Enjoy your meals!"
