# es.py
# This program reads in a text file and outputs the number of e's it contains
# Author: Hewa Orang
# reference: https://docs.python.org/3/library/sys.html

import sys  # Imports sys module to access the command-line argument
import os   # Imports os module to work with file and operating system operations

# Check if the user provided a filepath as an argument to our script
if len(sys.argv) < 2:
    print("Error: Please provide filepath") 
    exit(1) # exit the program 

file_name = sys.argv[1]   # get the filename from the command line argument

if not os.path.exists(file_name):   # Check if the file exists
    print("Error: filepath: {} doesn't exists!".format(file_name))
    exit(1)     #exit the program if filename not found


with open(file_name, 'r') as f:         # open the file in read mode
    letter = f.read()                   # read the content of the file 
    e_count =letter.count('e')          # counts the number of times letter e appears
    print("Number of e's:", e_count)    # prints the count

