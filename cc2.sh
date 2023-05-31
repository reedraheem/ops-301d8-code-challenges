#!/bin/bash

# Script:   code challenge 2                   
# Author: Raheem Sharif Reed                     
# Date of latest revision: may 31,2023     
# Purpose:Create a bash script that:Copies /var/log/syslog to the current working directory and Appends the current date and time to the filename

           
cp /var/log/syslog .

echo "syslog copied to $(pwd)"

current_date=$(date +"%Y-%m-%d_%H-%M-%S")
filename="syslog_${31may2023}"

cp /var/log/syslog "${filename}"

echo "syslog copied to ${filename}"

