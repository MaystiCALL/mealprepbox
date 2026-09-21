# === Stage 31: Add compact table rendering for long lists ===
# Project: MealPrepBox
def render_compact_table(items, columns):
    """Render a compact table for long lists.
    Args:
        items: List of dicts, each with keys matching columns.
        columns: List of column names.
    Returns:
        A formatted string representation of the table.
    """
    if not items:
        return "No items to display."
    
    header = " | ".join(columns)
    separator = "-+-".join(["-" * 10 for _ in columns])
    
    rows = []
    for item in items:
        row_values = [str(item.get(col, "")) for col in columns]
        rows.append(" | ".join(row_values))
    
    table = f"{header}\n{separator}\n" + "\n".join(rows)
    return table
