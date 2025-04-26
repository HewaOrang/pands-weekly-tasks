# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Hewa Orang
# reference: https://docs.python.org/3/library/calendar.html#cmdoption-calendar-first-weekday


import datetime # Imports the datetime module
import calendar # Imports the calendar module

date = datetime.date.today() # getting today's date using today() method 
weekday_name = calendar.day_name[date.weekday()] # Finding the name of weekday
# print(weekday_name)

if weekday_name in ("Saturday", "Sunday"): # Checking if today is weekend print below
    print ("It is the weekend, yay!")
else:                                      # If is week day print below
    print ("Yes, unfortunately today is a weekday")