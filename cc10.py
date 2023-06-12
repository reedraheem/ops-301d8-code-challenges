#Script:   code challenge 10              
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 12,2023     
# Purpose:Using file handling commands, create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.





import os

# Create a new .txt file
open('senpai.txt', 'w').close()

# Append three lines to the file
with open('senpai.txt', 'a') as file:
    file.write("This is line 1.\n")
    file.write("This is line 2.\n")
    file.write("This is line 3.\n")

# Print the first line to the screen
with open('senpai.txt', 'r') as file:
    lines = file.readlines()
    print(lines[0])

# Delete the .txt file
os.remove('senpai.txt')
