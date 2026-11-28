# === Stage 72: Add Markdown report export ===
# Project: MealPrepBox
def export_markdown(db):
    lines = ["# MealPrepBox Report", ""]
    for meal in db["meals"]:
        lines.append(f"## {meal['name']}")
        lines.append("")
        for b in db["batches"].get(meal["id"], []):
            lines.append(f"- Batch: {b['batch']} | Containers: {b['containers']}")
        lines.append("")
        for item in db["freezer"].get(meal["id"], []):
            lines.append(f"- Frozen: {item['item']} ({item['qty']} units)")
        lines.append("")
        for note in db["reheat"].get(meal["id"], []):
            lines.append(f"- Reheat: {note['method']} at {note['temp']}°C for {note['time']} min")
        lines.append("")
    with open("mealprep_report.md", "w") as f:
        f.write("\n".join(lines))
