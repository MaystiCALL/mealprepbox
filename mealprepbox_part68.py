# === Stage 68: Add a compact changelog generated from the activity log ===
# Project: MealPrepBox
def generate_changelog(activity_log):
    entries = sorted(activity_log, key=lambda e: e['date'], reverse=True)
    grouped = {}
    for entry in entries:
        grouped.setdefault(entry['date'], []).append(entry)
    lines = ["# MealPrepBox Changelog"]
    for date, changes in grouped.items():
        lines.append("")
        lines.append(f"## {date}")
        for change in changes:
            lines.append(f"- {change['action']}: {change['description']}")
    return "\n".join(lines)
