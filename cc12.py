#!/usr/bin/python3

# Script:   code challenge 12              
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 14,2023     
# Purpose:Create a Python script that performs the following:
#Prompt the user to type a string input as the variable for your destination URL.
#Prompt the user to select a HTTP Method of the following options:
#GET
#POST
#PUT
#DELETE
#HEAD
#PATCH
#OPTIONS
#Print to the screen the entire request your script is about to send. Ask the user to confirm before proceeding.
#Using the requests library, perform a GET request against your lab web server.
#For the given header, translate the codes into plain terms that print to the screen; for example, a 404 error should print Site not found to the terminal instead of 404.
#For the given URL, print response header information to the screen.

import requests

destination_url = input("Enter the destination URL: ")
http_method = input("Select an HTTP Method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

print("Request to be sent:")
print(http_method + " " + destination_url)

confirmation = input("Proceed with the request? (Y/N): ")
if confirmation.upper() == "Y":
    response = requests.request(http_method, destination_url)

    print("Request Headers:")
    for key, value in response.request.headers.items():
        print(key + ": " + value)

    print("\nResponse Headers:")
    for key, value in response.headers.items():
        print(key + ": " + value)

    print("\nResponse Content:")
    print(response.text)
else:
    print("Request canceled.")
