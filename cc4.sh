#!/bin/bash

# Reference:Chat GPT Assisted

# Script:   code challenge 4                  
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 2,2023     
# Purpose:Create a bash script that launches a menu system with the following options:
# Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)exit
#Next, the user input should be requested.
#The program should next use a conditional statement to evaluate the user’s input, then act according to what the user selected.
#Use a loop to bring up the menu again after the request has been executed.

#!/bin/bash

while true; do
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please try again."
            ;;
    esac

    echo
done
