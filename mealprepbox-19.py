# === Stage 19: Add undo support for the last simple mutation ===
# Project: MealPrepBox
class UndoableBatch:
    def __init__(self, name, meals, containers, freezer_inventory, reheating_notes):
        self.name = name
        self.meals = meals
        self.containers = containers
        self.freezer_inventory = freezer_inventory
        self.reheating_notes = reheating_notes
        self.undo_stack = []
        self.redo_stack = []

    def _snapshot(self):
        snapshot = {
            'meals': list(self.meals),
            'containers': list(self.containers),
            'freezer_inventory': list(self.freezer_inventory),
            'reheating_notes': dict(self.reheating_notes),
        }
        self.undo_stack.append(snapshot)
        self.redo_stack.clear()

    def add_meal(self, meal):
        self._snapshot()
        self.meals.append(meal)
        return meal

    def remove_meal(self, meal):
        self._snapshot()
        self.meals.remove(meal)
        return meal

    def add_container(self, container):
        self._snapshot()
        self.containers.append(container)
        return container

    def remove_container(self, container):
        self._snapshot()
        self.containers.remove(container)
        return container

    def update_freezer_inventory(self, item, quantity):
        self._snapshot()
        if item in self.freezer_inventory:
            self.freezer_inventory[self.freezer_inventory.index(item)] = quantity
        else:
            self.freezer_inventory.append(item)
        return self.freezer_inventory

    def add_reheating_note(self, meal, note):
        self._snapshot()
        self.reheating_notes[meal] = note
        return note
