# === Stage 17: Add dry-run behavior for commands that mutate state ===
# Project: MealPrepBox
def dry_run(command, state):
    """Simulate a mutating command without applying it.
    
    Args:
        command: The command string to simulate.
        state: The current state dictionary.
    
    Returns:
        A tuple of (success: bool, message: str, new_state: dict or None).
    """
    try:
        if command.startswith("add_batch"):
            parts = command.split()
            if len(parts) >= 3:
                batch_name = parts[1]
                quantity = int(parts[2])
                state.setdefault("batches", {})[batch_name] = quantity
                return True, f"Dry run: batch '{batch_name}' added with quantity {quantity}", state
            else:
                return False, "Invalid add_batch command", state
        elif command.startswith("add_container"):
            parts = command.split()
            if len(parts) >= 3:
                container_type = parts[1]
                capacity = int(parts[2])
                state.setdefault("containers", {})[container_type] = capacity
                return True, f"Dry run: container '{container_type}' added with capacity {capacity}", state
            else:
                return False, "Invalid add_container command", state
        elif command.startswith("add_freezer_item"):
            parts = command.split()
            if len(parts) >= 4:
                item_name = parts[1]
                quantity = int(parts[2])
                expiry_date = parts[3]
                state.setdefault("freezer", {})[item_name] = {"quantity": quantity, "expiry_date": expiry_date}
                return True, f"Dry run: freezer item '{item_name}' added with expiry {expiry_date}", state
            else:
                return False, "Invalid add_freezer_item command", state
        elif command.startswith("add_reheat_note"):
            parts = command.split()
            if len(parts) >= 4:
                item_name = parts[1]
                note = " ".join(parts[2:])
                state.setdefault("reheat_notes", {})[item_name] = note
                return True, f"Dry run: reheat note added for '{item_name}'", state
            else:
                return False, "Invalid add_reheat_note command", state
        else:
            return False, f"Unknown command: {command}", state
    except Exception as e:
        return False, f"Error during dry run: {str(e)}", state
