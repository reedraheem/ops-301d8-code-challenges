#!/usr/bin/env python3

# Reference:Chat GPT Assisted

# Script:   code challenge 7                
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 7,2023     
# Purpose:Create a Python script that generates all directories, sub-directories and files for a user-provided directory path.
#Script must ask the user for a file path and read a user input string into a variable.
#Script must use the os.walk() function from the os library.
#Script must enclose the os.walk() function within a python function that hands it the user input file path.


# Import libraries

import os

# Declaration of variables

### Read user input here into a variable

# Declaration of functions

### Declare a function here


def generate_directories_files(directory_path):
    for root, directories, files in os.walk(directory_path):
        print(f"Directory: {root}")
        for file in files:
            print(f"File: {os.path.join(root, file)}")

# Main

### Pass the variable into the function here

def main():
    user_path = input("Enter a directory path: ")
    generate_directories_files(user_path)

if __name__ == "__main__":
    main()

#end










