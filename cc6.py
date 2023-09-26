#!/usr/bin/python3

# Script:   code challenge 6                 
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 6,2023     
# Purpose:The Python module “os” must be utilized
#At least three variables must be declared in Python that contain results of bash operations
#The Python function print() must be used at least three times
#Include execution of the following bash commands inside your Python script:whoami, ip a, lshw -short



import os

# Execute Bash commands using os module
whoami_result = os.popen("whoami").read().strip()
ip_result = os.popen("ip a").read().strip()
lshw_result = os.popen("lshw -short").read().strip()

# Print the results
print("Current user:", whoami_result)
print("IP addresses:")
print(ip_result)
print("Hardware information:")
print(lshw_result)
