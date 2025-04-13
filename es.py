# es.py
# This program reads in a text file and outputs the number of e's it contains
# Author: Hewa Orang



FILENAME = "moby-dick.txt"


with open(FILENAME, 'r') as f:
    letter = f.read()
    e_count =letter.count('e')
    print("Number of e's:", e_count)

