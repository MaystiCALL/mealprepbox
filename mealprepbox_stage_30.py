# === Stage 30: Add date parsing helpers with clear error messages ===
# Project: MealPrepBox
import re
from datetime import date, datetime

_DATE_FORMATS = [
    "%Y-%m-%d",
    "%m/%d/%Y",
    "%d-%m-%Y",
    "%Y/%m/%d",
    "%m-%d-%Y",
    "%d/%m/%Y",
]

def parse_date(raw, context="date"):
    """Parse a date string into a date object with helpful error messages."""
    if raw is None:
        raise ValueError(f"{context}: no date provided")
    raw = str(raw).strip()
    if not raw:
        raise ValueError(f"{context}: empty date string")
    for fmt in _DATE_FORMATS:
        try:
            return datetime.strptime(raw, fmt).date()
        except ValueError:
            continue
    raise ValueError(
        f"{context}: could not parse '{raw}'. "
        f"Accepted formats: {', '.join(_DATE_FORMATS)}"
    )
