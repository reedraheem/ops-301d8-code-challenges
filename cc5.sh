#!/bin/bash

# Reference:Chat GPT Assisted

# Script:   code challenge 5                
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 5,2023     
# Purpose:Write a bash script that performs the following tasks:
#Print to the screen the file size of the log files before compression
#Compress the contents of the log files listed below to a backup directory
#/var/log/syslog
#/var/log/wtmp
#The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS
#example: /var/log/backups/syslog-20220928081457.zip
#Clear#Compare the size of the compressed files to the size of the original log files


# Function to print file size
print_file_size() {
    local file=$1
    local size=$(du -sh "$file" | cut -f1)
    echo "File size of $file: $size"
}

# Backup directory
backup_dir="/path/to/backup/directory"

# Log files
log_files=(
    "/var/log/syslog"
    "/var/log/wtmp"
)

# Get current timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Loop through log files
for file in "${log_files[@]}"; do
    # Print original file size
    print_file_size "$file"

    # Compress file to backup directory with timestamp
    compressed_file="$backup_dir/$(basename "$file").$timestamp.tar.gz"
    tar -czf "$compressed_file" "$file"

    # Clear the log file
    echo -n "" > "$file"

    # Print compressed file size
    print_file_size "$compressed_file"

    # Compare sizes
    original_size=$(du -s "$file" | cut -f1)
    compressed_size=$(du -s "$compressed_file" | cut -f1)
    echo "Comparison: Original size - $original_size, Compressed size - $compressed_size"
done
