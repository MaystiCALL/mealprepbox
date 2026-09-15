# === Stage 21: Add archive and restore behavior for completed or old records ===
# Project: MealPrepBox
def archive_records(records, cutoff_days=365):
    """Move records older than cutoff_days to an archive list."""
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=cutoff_days)
    archived = [r for r in records if r.get("completed_date") and r["completed_date"] < cutoff]
    active = [r for r in records if r not in archived]
    return active, archived

def restore_records(archived, cutoff_days=365):
    """Return records that are still within the active window."""
    import datetime
    cutoff = datetime.date.today() - datetime.timedelta(days=cutoff_days)
    return [r for r in archived if r.get("completed_date") and r["completed_date"] >= cutoff]
