# === Stage 40: Add plain text report export ===
# Project: MealPrepBox
def export_report(data, filename="meal_prep_report.txt"):
    lines = []
    lines.append("MealPrepBox Report")
    lines.append("=" * 30)
    lines.append(f"Batches: {len(data['batches'])}")
    lines.append(f"Containers: {len(data['containers'])}")
    lines.append(f"Freezer items: {len(data['freezer'])}")
    lines.append("")
    for batch in data["batches"]:
        lines.append(f"Batch: {batch['name']} ({batch['count']} servings)")
        for note in batch.get("reheating_notes", []):
            lines.append(f"  - {note}")
        lines.append("")
    for item in data["containers"]:
        lines.append(f"Container: {item['name']} ({item['size']} units)")
        lines.append("")
    for meal, days in data["freezer"].items():
        lines.append(f"{meal}: frozen for {days} days")
    with open(filename, "w") as f:
        f.write("\n".join(lines))
