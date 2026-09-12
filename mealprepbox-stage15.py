# === Stage 15: Add a simple command dispatcher for text commands ===
# Project: MealPrepBox
class MealPrepCommandDispatcher:
    """Dispatches simple text commands for MealPrepBox."""
    COMMANDS = {
        'add': lambda args: (True, 'Added new batch.'),
        'remove': lambda args: (True, 'Batch removed.'),
        'list': lambda args: (True, 'Showing all batches.'),
        'freezer': lambda args: (True, 'Freezer inventory updated.'),
        'help': lambda args: (True, 'Available commands: add, remove, list, freezer, help'),
        'status': lambda args: (True, 'MealPrepBox is ready.'),
    }
    @classmethod
    def run(cls, text):
        if not text or text.strip() == '':
            return (False, 'Please enter a command.')
        parts = text.strip().split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1].split() if len(parts) > 1 else []
        handler = cls.COMMANDS.get(cmd)
        if handler is None:
            return (False, f'Unknown command: {cmd}. Type "help" for a list.')
        return handler(args)
