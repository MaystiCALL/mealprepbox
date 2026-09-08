# === Stage 7: Add list and detail formatting helpers for console output ===
# Project: MealPrepBox
def format_batch_summary(batch):
    lines = [f"Batch: {batch['name']}"]
    if 'recipe' in batch:
        lines.append(f"  Recipe: {batch['recipe']}")
    if 'containers' in batch:
        lines.append(f"  Containers: {len(batch['containers'])} ({', '.join(batch['containers'])})")
    if 'notes' in batch:
        lines.append(f"  Notes: {batch['notes']}")
    return '\n'.join(lines)

def format_freezer_summary(freezer):
    lines = [f"Freezer Inventory:"]
    for item in freezer['items']:
        lines.append(f"  - {item['name']}: {item['quantity']}x {item['unit']}")
    if 'total_space' in freezer:
        lines.append(f"  Total space used: {freezer['total_space']}")
    return '\n'.join(lines)
