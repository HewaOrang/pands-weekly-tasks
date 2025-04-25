# es.py
# This program reads in a text file and outputs the number of e's it contains
# Author: Hewa Orang
# reference: https://docs.python.org/3/library/sys.html

import sys  
import os

# make sure the user provided a filepath as an argument to our script
if len(sys.argv) < 2:
    print("Error: Please provide filepath")
    exit(1)
# 
file_name = sys.argv[1]

if not os.path.exists(file_name):
    print("Error: filepath: {} doesn't exists!".format(file_name))
    exit(1)

# FILENAME = input("enter your file name")

with open(file_name, 'r') as f:
    letter = f.read()
    e_count =letter.count('e')
    print("Number of e's:", e_count)

