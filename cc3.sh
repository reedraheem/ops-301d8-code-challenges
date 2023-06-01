#!/bin/bash

# Reference: Chat GPT

# Script:   code challenge 3                  
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 1,2023     
# Purpose:Create a new bash script that performs the following:
#Prompts user for input directory path.
#Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#Navigates to the directory input by the user and changes all files inside it to the input setting.
#Prints to the screen the directory contents and the new permissions settings of everything in the directory.


# Prompt user for input directory path
read -p "Enter the directory path: " directory

# Check if the directory exists
if [ -d "$anime96" ]; then
  echo "Directory '$anime96' exists."
else
  echo "Directory '$anime96' does not exist."
fi

# Prompt the user for the permissions number
read -p "Enter permissions number: " permissions

# Validate the input
if ! [[ $permissions =~ ^[0-7]{1}$ ]]; then
    echo "Invalid permissions number. Please enter a single digit between 0 and 7."
    exit 1
fi

# Display the input permissions number
echo "Input permissions number: $permissions"


# Prompt the user to input a directory path
read -p "Enter the directory path: " directory

# Check if the directory exists
if [ -d "$anime96" ]; then
    # Navigate to the specified directory
    cd "$anime96"
    
    # Prompt the user to input the setting for the files
    read -p "Enter the desired setting for the files: " setting
    
    # Change the setting for all files in the directory
    chmod "$setting" *
    
    echo "File settings changed successfully."
else
    echo "Directory not found."
fi


anime96="/path/to/directory"

# Print directory contents
echo "Directory Contents:"
ls "$anime96"

# Loop through each item in the directory
for item in "$anime96"/*
do
  if [ -f "$item" ] || [ -d "$item" ]; then
    # Get current permissions
    old_permissions=$(stat -c "%a" "$item")

    # Set new permissions
    chmod 755 "$item"

    # Get new permissions
    new_permissions=$(stat -c "%a" "$item")

    # Print item and permissions
    echo "Item: $item"
    echo "Old Permissions: $old_permissions"
    echo "New Permissions: $new_permissions"
    echo "------------------------------"
  fi
done


