# squareroot.py
# This program takes a positive float number and outputs its square root.
# Author: Hewa Orang
# Reference: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm


num= float(input("Enter a number"))
approx = 0.5*num
better=0.5*(approx+num/approx)

while better != approx:
    approx=better
    better=0.5*(approx+num/approx)

print(f" Square Root {better}")

