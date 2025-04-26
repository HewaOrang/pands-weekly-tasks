# collatz.py
# This program prompts the user to input a positive int and outputs the values after applying following calcs
# If the number is even divide it by two ; if it's odd multiply by three and add one
# Reference: https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence#:~:text=If%20n%20is%20even%2C%20divide,will%20always%20eventually%20reach%201.
# Author: Hewa Orang

# Prompts the user to input integer number
number = int(input("Please enter a positive integer:"))

print(number, end= " ") # Prints the starting number and output to stay at the same line.

while number > 1: # starts a loop that continues as long as the number is >1
    if number % 2 == 0: # if the number is even, divide it by 2
        number = number//2
    else:
        number = 3*number +1 # if the number is odd x3 and add 1 
    print(number, end= " ") # print the number on the same line
