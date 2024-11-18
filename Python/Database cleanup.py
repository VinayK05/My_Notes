import os
import time

database_name = "your_database"
days_to_keep = 7

backup_dir = "/path/to/database/backups"
cutoff_time = time.time() - days_to_keep * 24 * 60 * 60

for root, _, files in os.walk(backup_dir):
    for file in files:
        if file.startswith(database_name) and file.endswith(".sql"):
            file_path = os.path.join(root, file)
            file_mtime = os.path.getmtime(file_path)
            if file_mtime < cutoff_time:
                os.remove(file_path)
                print(f"Removed old backup: {file_path}")

print("Old database backups cleaned up.")
