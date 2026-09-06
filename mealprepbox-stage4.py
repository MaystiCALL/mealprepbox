# === Stage 4: Implement create operations for the primary records ===
# Project: MealPrepBox
def create_meal_plan(plan, meal, batch, container, freezer, note):
    """Create a meal plan with all its components."""
    meal_plan = MealPlan(
        id=plan.id,
        name=plan.name,
        created_at=plan.created_at,
        updated_at=plan.updated_at,
    )
    meal_plan.meal = meal
    meal_plan.batch = batch
    meal_plan.container = container
    meal_plan.freezer = freezer
    meal_plan.note = note
    return meal_plan

def create_meal(meal, batch):
    """Create a meal with its batch."""
    return Meal(
        id=meal.id,
        name=meal.name,
        calories=meal.calories,
        protein=meal.protein,
        carbs=meal.carbs,
        fat=meal.fat,
        created_at=meal.created_at,
        updated_at=meal.updated_at,
        batch=batch,
    )

def create_batch(batch, meal):
    """Create a batch with its meal."""
    return Batch(
        id=batch.id,
        name=batch.name,
        servings=batch.servings,
        prep_time=batch.prep_time,
        created_at=batch.created_at,
        updated_at=batch.updated_at,
        meal=meal,
    )

def create_container(container, meal):
    """Create a container with its meal."""
    return Container(
        id=container.id,
        name=container.name,
        volume=container.volume,
        material=container.material,
        created_at=container.created_at,
        updated_at=container.updated_at,
        meal=meal,
    )

def create_freezer(freezer, meal):
    """Create a freezer with its meal."""
    return Freezer(
        id=freezer.id,
        name=freezer.name,
        capacity=freezer.capacity,
        location=freezer.location,
        created_at=freezer.created_at,
        updated_at=freezer.updated_at,
        meal=meal,
    )

def create_note(note, meal):
    """Create a note with its meal."""
    return Note(
        id=note.id,
        text=note.text,
        created_at=note.created_at,
        updated_at=note.updated_at,
        meal=meal,
    )
