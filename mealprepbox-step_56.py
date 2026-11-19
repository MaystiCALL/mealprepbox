# === Stage 56: Add compact error classes for domain failures ===
# Project: MealPrepBox
class MealPrepError(Exception):
    pass


class RecipeNotFoundError(MealPrepError):
    def __init__(self, recipe_id):
        self.recipe_id = recipe_id
        super().__init__(f"Recipe {recipe_id} not found")


class BatchExpiryError(MealPrepError):
    def __init__(self, batch_id, days_left):
        self.batch_id = batch_id
        self.days_left = days_left
        super().__init__(f"Batch {batch_id} expires in {days_left} days")


class ContainerCapacityError(MealPrepError):
    def __init__(self, container_id, required, available):
        self.container_id = container_id
        self.required = required
        self.available = available
        super().__init__(
            f"Container {container_id} needs {required} units but only {available} available"
        )


class ReheatTemperatureError(MealPrepError):
    def __init__(self, target_temp, min_temp, max_temp):
        self.target_temp = target_temp
        self.min_temp = min_temp
        self.max_temp = max_temp
        super().__init__(
            f"Reheat temperature {target_temp} outside safe range {min_temp}-{max_temp}"
        )


class FreezerFullError(MealPrepError):
    def __init__(self, freezer_id, required_slots, available_slots):
        self.freezer_id = freezer_id
        self.required_slots = required_slots
        self.available_slots = available_slots
        super().__init__(
            f"Freezer {freezer_id} needs {required_slots} slots but only {available_slots} available"
        )
