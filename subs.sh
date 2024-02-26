#!/bin/bash

# Parent directory containing the files
parent_dir="."

# Maximum number of files per subdirectory
max_files=700

# Counter for subdirectory naming
dir_counter=1

# Counter for keeping track of the number of files processed
file_counter=0

# Create the first subdirectory
mkdir -p "${parent_dir}/strips${dir_counter}"

# Loop through files in the parent directory
for file in "${parent_dir}"/*; do
  # Copy file to the current subdirectory
  cp "$file" "${parent_dir}/strips${dir_counter}/"
  
  # Increment file counter
  ((file_counter++))
  
  # Check if the current subdirectory has reached its max capacity
  if [ "$file_counter" -eq "$max_files" ]; then
    # Reset file counter
    file_counter=0
    
    # Increment directory counter
    ((dir_counter++))
    
    # Create a new subdirectory
    mkdir -p "${parent_dir}/strips${dir_counter}"
  fi
done
