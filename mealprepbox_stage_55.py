# === Stage 55: Add a setting to disable colorized output ===
# Project: MealPrepBox
COLOR_ENABLED = getattr(
    __import__("os").environ, "MEAL_PREP_COLOR", "1"
) == "1"


def _colorize(text, code):
    if not COLOR_ENABLED:
        return text
    return "\033[{}m{}\033[0m".format(code, text)


def colorize(text, code):
    return _colorize(text, code)


def green(text):
    return _colorize(text, "\033[32m")


def red(text):
    return _colorize(text, "\033[31m")


def yellow(text):
    return _colorize(text, "\033[33m")


def cyan(text):
    return _colorize(text, "\033[36m")


def bold(text):
    return _colorize(text, "\033[1m")


def dim(text):
    return _colorize(text, "\033[2m")


def header(text):
    return bold(cyan(text))


def warning(text):
    return red(bold(text))


def success(text):
    return green(bold(text))


def info(text):
    return cyan(text)


def muted(text):
    return dim(text)


def color_enabled():
    return COLOR_ENABLED
