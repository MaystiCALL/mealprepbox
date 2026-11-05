# === Stage 41: Add plain text import for a simple line-based format ===
# Project: MealPrepBox
import csv


def load_plain(path):
    rows = []
    with open(path, newline="") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",", 3)
            if len(parts) < 4:
                continue
            rows.append({
                "name": parts[0].strip(),
                "batch": parts[1].strip(),
                "containers": int(parts[2].strip()) if parts[2].strip().isdigit() else 0,
                "frozen": parts[3].strip(),
            })
    return rows


def save_plain(path, meals):
    lines = []
    for meal in meals:
        lines.append("{},{},{},{}".format(
            meal["name"],
            meal["batch"],
            meal.get("containers", 0),
            meal.get("frozen", ""),
        ))
    with open(path, "w") as handle:
        handle.write("\n".join(lines) + "\n")
