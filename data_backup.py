import shutil
import os

# Paths
source_file = "final_data.csv"
backup_dir = "backup"

# Create backup directory if it doesn't exist
if not os.path.exists(backup_dir):
    os.makedirs(backup_dir)

# Define backup file path
backup_file = os.path.join(backup_dir, "final_data_backup.csv")

# Copy the file
shutil.copy2(source_file, backup_file)

print(f"Backup completed: {backup_file}")
