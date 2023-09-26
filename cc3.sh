#!/bin/bash



# Script:   code challenge 3                 
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 1,2023   

#Purpose:Create a new bash script that performs the following:
#Prompts user for input directory path.
#Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#Navigates to the directory input by the user and changes all files inside it to the input setting.
#Prints to the screen the directory contents and the new permissions settings of everything in the directory.


# Prompt user for input directory path
read -p "ops-301d8-code-challenges: " directory

# Prompt user for input permissions number
read -p "777: " permissions

# Change permissions of files in the directory
find $directory -type f -exec chmod $permissions {} +

# Print directory contents and permissions
ls -l $directory



