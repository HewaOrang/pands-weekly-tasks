# squareroot.py
# This program takes a positive float number and outputs its square root.
# Author: Hewa Orang
# Reference: https://stackoverflow.com/questions/28733759/python-square-function-using-newtons-algorithm


num= float(input("Enter a number")) # Take input and convert it to a float
approx = 0.5*num                    # Initial guess 0.5 of num
better=0.5*(approx+num/approx)      # Improving the guess by using ave of approx and num/approx

while better != approx:             # while statement keep improving the guess until approx == better
    approx=better
    better=0.5*(approx+num/approx)

print(f" Square Root {better}")     # prints the final improved value

