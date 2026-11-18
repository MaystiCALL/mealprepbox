# === Stage 54: Add colorized output through optional ANSI codes ===
# Project: MealPrepBox
def colorize(text, code):
    """Wrap text with ANSI color codes and restore default on output end."""
    return f"\033[{code}m{text}\033[0m"

COLORS = {
    "header": "1;96",
    "ok": "1;32",
    "warn": "1;33",
    "error": "1;31",
    "info": "1;34",
    "muted": "2",
    "bold": "1",
}

class Ctx:
    def __init__(self, enabled=True):
        self.enabled = enabled
    def __call__(self, text, code=None):
        if not self.enabled or code is None:
            return text
        return colorize(text, code)

def style(text, name):
    return Ctx()(text, COLORS.get(name))

def print_header(title):
    print()
    print(style(title, "header"))
    print(style("=" * len(title), "muted"))

def print_ok(msg):
    print(style(msg, "ok"))

def print_warn(msg):
    print(style(msg, "warn"))

def print_error(msg):
    print(style(msg, "error"))

def print_info(msg):
    print(style(msg, "info"))

def print_muted(msg):
    print(style(msg, "muted"))

def print_bold(msg):
    print(style(msg, "bold"))

def banner(text):
    print_header(text)
    print(style("MealPrepBox v1.0", "bold"))
    print_muted("Batch  |  Containers  |  Freezer  |  Reheat")
