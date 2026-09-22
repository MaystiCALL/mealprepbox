# === Stage 33: Add a settings dictionary and functions to update settings ===
# Project: MealPrepBox
def add_settings():
    settings = {}
    settings["container_size"] = 500  # ml
    settings["freezer_label_format"] = "{meal_name} - {date}"
    settings["reheat_temp"] = 180  # degrees Celsius
    settings["reheat_time"] = 20  # minutes
    settings["batch_default"] = 4  # people
    return settings
