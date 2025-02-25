# account.py
# This program reads in acc no. of any length and 
# outputs the last 4 digits and the first 6 digits replaced with Xs 
# Author: Hewa Orang
# references: https://stackoverflow.com/questions/26921164/how-to-apply-a-custom-mask-into-a-string-of-digits-in-python
#     https://docs.python.org/3/library/stdtypes.html#string-methods         

account_number = (input ("Please enter a 10 digit account number:"))

if account_number.isdigit():
    masked_part = "X" * max(0, len(account_number) -4)
    print(f"{masked_part}{account_number[-4:]}")
else:
    print(f"invalid input! Please enter a numeric account number.")



