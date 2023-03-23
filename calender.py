import calendar

month = 1
while month < 13:
    print(calendar.month(2023, month)) 
    month += 1


def year():
    print(calendar.calendar(2023))

def month():
    print(calendar.month(2023, 2)) 

def gap():
    print(calendar.month(2023, 2, 5))


