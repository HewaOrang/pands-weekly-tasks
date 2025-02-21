# account.py
# This program reads in a 10 chara. acc no. and 
# outputs the last 4 digits and the first 6 digits replaced with Xs 
# Author: Hewa Orang
# references: https://stackoverflow.com/questions/26921164/how-to-apply-a-custom-mask-into-a-string-of-digits-in-python
#              

accountNumber = (input ("Please enter a 10 digit account number:"))
masked = "X" * 6
print(f"{masked}{accountNumber[6:]}")



