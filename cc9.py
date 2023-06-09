# Reference:Chat GPT Assisted

# Script:   code challenge 9               
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 9,2023     
# Purpose:Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
#Equals: a == b
#Not Equals: a != b
#Less than: a < b
#Less than or equal to: a <= b
#Greater than: a > b
#Greater than or equal to: a >= b
#Create an if statement using a logical conditional of your choice and include elif keyword that executes when other conditions are not met.
#Create an if statement that includes both elif and else to execute when both if and elif are not met.


# Equals
x = 5
if x == 5:
    print("x is equal to 5")

# Not Equals
y = 10
if y != 5:
    print("y is not equal to 5")

# Less than
z = 8
if z < 10:
    print("z is less than 10")

# Less than or equal to
a = 15
if a <= 20:
    print("a is less than or equal to 20")

# Greater than
b = 25
if b > 20:
    print("b is greater than 20")

# Greater than or equal to
c = 30
if c >= 30:
    print("c is greater than or equal to 30")

# If statement with elif
num = 7
if num < 5:
    print("Number is less than 5")
elif num > 10:
    print("Number is greater than 10")
else:
    print("Number is between 5 and 10")

# If statement with elif and else
grade = 75
if grade >= 90:
    print("Grade is A")
elif grade >= 80:
    print("Grade is B")
elif grade >= 70:
    print("Grade is C")
else:
    print("Grade is below C")
