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


#Explanation:

Import necessary modules:

os: Provides functions for interacting with the operating system, including file operations.
time: Provides functions for working with time, including calculating time differences.
Define variables:

database_name: The name of the database.
days_to_keep: The number of days to keep backups.
backup_dir: The directory where backups are stored.
cutoff_time: A timestamp calculated by subtracting days_to_keep days from the current time.
Iterate through backup directory:

os.walk(backup_dir) recursively iterates through the backup directory and its subdirectories.
For each file in the directory:
Check if the file name starts with database_name and ends with .sql.
Get the modification time of the file using os.path.getmtime(file_path).
If the modification time is older than the cutoff_time, remove the file using os.remove(file_path).
Print a completion message:

After processing all files, print a message indicating that the cleanup is complete.
Key differences between Bash and Python:

Looping: Bash uses find and exec to locate and remove files, while Python uses a more explicit loop and file operations.
Time calculations: Bash uses mtime to check file modification time, while Python uses time.time() and time differences.
Error handling: Python can include more robust error handling mechanisms, such as using try-except blocks.
Readability: Python's syntax is often considered more readable and maintainable than Bash, especially for complex scripts.
This Python script provides a more structured and flexible approach to cleaning up old database backups, offering better control and error handling. ###
