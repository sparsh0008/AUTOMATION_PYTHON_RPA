from datetime import *

a = datetime.now()
print("Date : {}/{}/{} ".format(a.day, a.month, a.year))
print("Time : {}:{}:{}".format(a.hour, a.minute, a.second))

FormatString = a.strftime("%d, %b, %Y - %A")
print(FormatString)

print("\n")
b = datetime.now()
Date2 = b.strftime("Today Date - %d, %b, %Y")
year = b.strftime("Number of days till Today in %Y is - %j")
date1 = b.strftime("Today Date - %d")
FromatString1 = b.strftime('Today Day - %A')
print("{}\n{}\n{}\n{}".format(Date2, date1, FromatString1, year))

