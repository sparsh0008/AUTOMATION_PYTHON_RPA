# Sample Dates
# Date 1 - 12/02/1970
# Date 2 - 11/05/1968
from datetime import *

d1, m1, y1 = [int(x) for x in input("Enter the Date 1 : ").split('/')]
dt1 = date(y1, m1, d1)
print("Date - {}".format(dt1))
print(dt1.strftime("Day %w of the week is %A\n"))

d2, m2, y2 = [int(x) for x in input("Enter the Date 2 : ").split('/')]
dt2 = date(y2, m2, d2)
print("Date - {}".format(dt2))
print(dt2.strftime("Day %w of the week is %A\n"))

dateDifference = dt1 - dt2
todaydays = dateDifference.days
weeks, days = divmod(dateDifference.days, 7)

print("Difference between two days is {0} and total Number of weeks is {1} + {2} days left in same week".
      format(todaydays, weeks, days))

dt3 = datetime(2016, 4, 29, 16, 45, 0)
addDate = timedelta(days=10, seconds=10, minutes=20, hours=12)
print(dt3 + addDate)

dt4 = datetime(1996, 6, 26)
timeDate1 = timedelta(days=10)
print(timeDate1 + dt4)
