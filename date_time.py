import datetime
from datetime import date
now = datetime.datetime.now()
print(now)
current_date = datetime.date.today()
print(current_date)

d = datetime.date(2023, 3, 15)
print(d)

todays_date = date.today()
print("Today's date =", todays_date)

timestamp = date.fromtimestamp(77) 
print("Date =", timestamp)
today = date.today()

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
now = datetime.datetime.now()
t = now.strftime("%H:%M:%S")
print("Time:", t)
s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
print("s1:", s1)
s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
print("s2:", s2)

# To add days to present date and tell the date:
today = datetime.date.today()
day = int(input("Enter the number of days to add: "))
days = datetime.timedelta(days = day)
added_days = today + days
print(added_days)
