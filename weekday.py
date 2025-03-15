# weekday.py
# This program outputs whether or not today is a weekday.
# Author: Hewa Orang
# reference: https://docs.python.org/3/library/calendar.html#cmdoption-calendar-first-weekday


import datetime
import calendar

date = datetime.date.today()
weekday_name = calendar.day_name[date.weekday()]
# print(weekday_name)

if weekday_name in ("Saturday", "Sunday"):
    print ("It is the weekend, yay!")
else:
    print ("Yes, unfortunately today is a weekday")