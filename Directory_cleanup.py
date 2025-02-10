import os
import time

def cleanup_old_files(directory, days_old):
    # Get the current time
    current_time = time.time()
    
    # Calculate the time threshold in seconds
    time_threshold = current_time - (days_old * 86400)
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Check if the file is older than the threshold
        if os.path.isfile(file_path) and os.path.getmtime(file_path) < time_threshold:
            os.remove(file_path)
            print(f"Deleted: {file_path}")

# Set the directory and days_old
directory = "/path/to/directory"
days_old = 30

# Call the function to cleanup old files
cleanup_old_files(directory, days_old)
