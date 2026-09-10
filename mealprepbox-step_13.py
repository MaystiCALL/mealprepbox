# === Stage 13: Add file save support using a configurable path ===
# Project: MealPrepBox
import os
import json
from datetime import datetime

def save_plans(plans, path=None):
    if path is None:
        path = os.path.join(os.path.dirname(__file__) or '.', 'meal_prep.json')
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    safe_path = path.replace('/', '_').replace('\\', '_') + f'_{timestamp}.json'
    with open(safe_path, 'w') as f:
        json.dump(plans, f, indent=2)
    return safe_path
