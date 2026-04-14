import os
import shutil

def check_directory_health(target_path, size_threshold_mb=10):
    """
    Checks disk usage and lists files larger than a specific threshold.
    """
    # 1. Check Disk Usage
    try:
        # shutil.disk_usage returns total, used, and free bytes
        total, used, free = shutil.disk_usage(target_path)
        percent_used = (used / total) * 100
        print(f"--- Disk Health for {target_path} ---")
        print(f"Usage: {percent_used:.2f}%")
        print(f"Free Space: {free // (2**30)} GB\n")
    except FileNotFoundError:
        print(f"Error: The directory '{target_path}' was not found.")
        return
    except PermissionError:
        print(f"Error: No permission to access disk stats for '{target_path}'.")
        return

    # 2. List large files
    print(f"--- Files larger than {size_threshold_mb}MB ---")
    try:
        # Using os.scandir for better performance over os.listdir
        with os.scandir(target_path) as entries:
            for entry in entries:
                if entry.is_file():
                    # Convert bytes to megabytes
                    file_size_mb = entry.stat().st_size / (1024 * 1024)
                    if file_size_mb > size_threshold_mb:
                        print(f"File: {entry.name} | Size: {file_size_mb:.2f} MB")
    except PermissionError:
        print("Error: Permission denied while scanning files.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    # Using relative path to stay safe and portable
    # '.' refers to the current working directory (Documents/Google)
    my_folder = "."
    check_directory_health(my_folder)
