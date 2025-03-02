# collatz.py
# This program prompts the user to input a positive int and outputs the values after applying following calcs
# If the number is even divide it by two ; if it's odd multiply by three and add one
# Reference: https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence#:~:text=If%20n%20is%20even%2C%20divide,will%20always%20eventually%20reach%201.
# Author: Hewa Orang

number = int(input("Please enter a positive integer:"))

print(number, end= " ")

while number > 1:
    if number % 2 == 0:
        number = number//2
    else:
        number = 3*number +1
    print(number, end= " ")
