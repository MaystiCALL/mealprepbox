# === Stage 29: Add reminder helpers that return upcoming items ===
# Project: MealPrepBox
def upcoming_batches(batches, days_ahead=7):
    """Return batches due to finish within the next `days_ahead` days, sorted by deadline."""
    due = []
    for b in batches:
        days_left = b['deadline'] - b['start'] + 1
        if 0 < days_left <= days_ahead:
            due.append(b)
    return sorted(due, key=lambda x: x['deadline'])

def upcoming_freezer_expirations(items, days_ahead=30):
    """Return freezer items expiring within `days_ahead` days, sorted by expiry."""
    expiring = []
    for item in items:
        if item['frozen']:
            days_left = item['expiry'] - item['frozen_date'] + 1
            if 0 < days_left <= days_ahead:
                expiring.append(item)
    return sorted(expiring, key=lambda x: x['expiry'])

def upcoming_reheat_reminders(items):
    """Return items needing reheating within the next 3 days, sorted by reheat_date."""
    soon = []
    for item in items:
        if item.get('reheat_date') and item['reheat_date'] <= item['prepared'] + 3:
            soon.append(item)
    return sorted(soon, key=lambda x: x['reheat_date'])

def all_upcoming(batches, items, days_ahead=7):
    """Return all upcoming reminders as a single sorted list by earliest date."""
    reminders = []
    for b in upcoming_batches(batches, days_ahead):
        reminders.append({'type': 'batch_due', 'item': b, 'date': b['deadline']})
    for i in upcoming_freezer_expirations(items, days_ahead):
        reminders.append({'type': 'freezer_expiring', 'item': i, 'date': i['expiry']})
    for i in upcoming_reheat_reminders(items):
        reminders.append({'type': 'reheat_needed', 'item': i, 'date': i['reheat_date']})
    return sorted(reminders, key=lambda x: x['date'])
