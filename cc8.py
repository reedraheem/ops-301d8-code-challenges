#!/usr/bin/python3

#Script: code challenge 8               
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 7,2023     
# Purpose:Create a Python script that includes the following:
#Assign to a variable a list of ten string elements.
#Print the fourth element of the list.
#Print the sixth through tenth element of the list.
#Change the value of the seventh element to “onion”.

favorite_boxers =["Roy jones Jr", "Floyd Mayweather Jr", "Pernell Whitaker", "Andre Ward", "Winky Wright", "Terrance Crawford", "Dmitry Bivol", "Shakur stevenson", "Thomas hearns", "James Toney"]


print("Fourth element:", favorite_boxers[3])
print("Sixth to tenth elements:", favorite_boxers[5:10])

favorite_boxers[6] = "onion"

print("Updated list:", favorite_boxers)


