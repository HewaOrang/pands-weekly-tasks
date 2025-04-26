# bank.py
# This program reads in two amounts in cents and prints their sums out in euros
# Author: Hewa Orang


# This reads two values in cents
amount1 = int(input("Enter amount 1(in cent):"))
amount2 = int(input("Enter amount 2(in cent):"))

# This sums the values in cents
sum = (amount1 + amount2)

# Convert to euros (1 euro = 100 cents)
euros = sum / 100


print('The sum of this is €' , euros)


