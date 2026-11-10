# === Stage 44: Add backup creation for the data file ===
# Project: MealPrepBox
def save_backup(filepath, backup_dir="backups"):
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, "mealprepbox_backup_" + timestamp + ".json")
    with open(backup_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    return backup_path

def save_backup_now():
    return save_backup(DATA_FILE)

if __name__ == "__main__":
    print("Backup saved to:", save_backup_now())
