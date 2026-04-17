#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
set -e

# --- Script to prepare the environment and edit a file ---

# 1. Check for root privileges, required for 'apt-get'
if [ "$(id -u)" -ne 0 ]; then
  echo "This script must be run as root. Please use 'sudo ./setup_and_edit.sh'" >&2
  exit 1
fi

# 2. Check if nano is installed, and install it if not
if ! command -v nano &> /dev/null; then
    echo "--- Nano not found. Installing... ---"
    # Update package list. A good practice before installing.
    apt-get update
    # Install the 'nano' text editor. The -y flag auto-confirms.
    apt-get install -y nano
else
    echo "--- Nano is already installed. Skipping installation. ---"
fi

# 3. List files in the current directory in long format
echo "--- Listing files in the current directory... ---"
ls -l

# 4. Load the 'hello_world.py' file in the nano editor
# If the file does not exist, nano will create it upon saving.
echo "--- Abrindo hello_world.py no nano... ---"
nano hello_world.py

echo "--- Script finished. Nano editor has been closed. ---"