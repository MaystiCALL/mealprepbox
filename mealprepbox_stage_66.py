# === Stage 66: Add export of a short status dashboard ===
# Project: MealPrepBox
def print_status_dashboard(inventory):
    total = sum(len(b.containers) for b in inventory)
    frozen = sum(len(b.containers) for b in inventory if b.frozen)
    print("MealPrepBox Status Dashboard")
    print("-" * 28)
    print(f"Total containers : {total}")
    print(f"Frozen           : {frozen}")
    print(f"Fresh            : {total - frozen}")
    if inventory:
        longest = max(inventory, key=lambda b: len(b.containers))
        print(f"Most batches     : {longest.name} ({len(longest.containers)})")
        if longest.reheat_note:
            print(f"Reheat note      : {longest.reheat_note}")
    print("-" * 28)
