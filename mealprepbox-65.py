# === Stage 65: Add import merging behavior that avoids obvious duplicates ===
# Project: MealPrepBox
import re


def merge_imports(existing, new):
    lines = existing.splitlines()
    import_lines = []
    seen = set()
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if re.match(r"^\s*(import|from)\b", stripped):
            import_lines.append(stripped)
            seen.add(canonical(stripped))
        else:
            lines = lines[:lines.index(line)] + lines[line + 1:]
    for line in new:
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if re.match(r"^\s*(import|from)\b", stripped):
            key = canonical(stripped)
            if key in seen:
                continue
            seen.add(key)
            import_lines.append(stripped)
    return "\n".join(lines) + "\n" + "\n".join(import_lines) + "\n"


def canonical(line):
    line = line.strip()
    line = re.sub(r"\s*,", ",", line)
    line = line.replace(" as ", " as ").strip()
    line = re.sub(r"\s*\(\s*\)", "", line)
    return line.strip().lower()
