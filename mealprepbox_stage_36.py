# === Stage 36: Add templates for quickly creating common records ===
# Project: MealPrepBox
class RecordTemplates:
    """Pre-built record templates for common meal-prep scenarios."""

    def __init__(self, meal_plan, batch_manager, container_manager,
                 freezer_manager, reheater):
        self.meal_plan = meal_plan
        self.batch_manager = batch_manager
        self.container_manager = container_manager
        self.freezer_manager = freezer_manager
        self.reheater = reheater

    def quick_batch(self, recipe, servings, prep_date, batch_id=None):
        if batch_id is None:
            batch_id = f"batch_{servings}x{prep_date}"
        batch = self.batch_manager.create_batch(recipe, servings, prep_date, batch_id)
        return batch

    def quick_container(self, batch, container_id=None):
        if container_id is None:
            container_id = f"cont_{batch.batch_id}"
        container = self.container_manager.create_container(batch, container_id)
        return container

    def quick_freezer(self, batch, freeze_date, thaw_date, freezer_id=None):
        if freezer_id is None:
            freezer_id = f"freezer_{freeze_date}"
        freezer_entry = self.freezer_manager.create_freezer_entry(
            batch, freeze_date, thaw_date, freezer_id
        )
        return freezer_entry

    def quick_reheat(self, container, reheat_date, reheat_method="microwave",
                      reheat_notes=""):
        reheat_record = self.reheater.create_reheat_record(
            container, reheat_date, reheat_method, reheat_notes
        )
        return reheat_record

    def full_prep_cycle(self, recipe, servings, prep_date, container_id=None,
                        freeze_date=None, thaw_date=None, reheat_date=None,
                        reheat_method="microwave", reheat_notes=""):
        batch = self.quick_batch(recipe, servings, prep_date,
                                 f"full_{servings}x{prep_date}")
        container = self.quick_container(batch, container_id)
        if freeze_date and thaw_date:
            self.quick_freezer(batch, freeze_date, thaw_date)
        if reheat_date:
            self.quick_reheat(container, reheat_date, reheat_method, reheat_notes)
        return batch, container
