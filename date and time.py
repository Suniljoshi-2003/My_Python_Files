# python date
import datetime
x = datetime.datetime.now()
print(x)

# Create Date Object 
#  (yyyy mm dd)
x = datetime.datetime(2024, 9, 15)
print(x)

x= datetime.datetime(2024, 9,15)
print(x)


# symbels -->

# %b Month_name, short version Dec
#  %B Month_name , Full Version December
# %m Month as number 01-12   12
# %y Year, sort version, without century  18
# %Y year , full version  2018
# %H Hour 00-23 17
# %I Hour 00-12   05
# %p AM/PM  PM
# %M Minute 00-59  41
#  %s secound


now = datetime.datetime.now()
year = now.strftime("%Y")
print("year:",year)




import datetime

x = datetime.datetime.now()
m = x.strftime("%y")   # year
Y = x.strftime("%Y")
print(x)
print(m)
print(Y)

Month_s = x.strftime("%b")
print(Month_s)
Month_f = x.strftime("%B")
print(Month_f)

Month_num = x.strftime("%m")  # month 
print(Month_num)

Minuts = x.strftime("%M")
print(Minuts)

Time_24 = x.strftime("%H") # 24 houres acording timw
print(Time_24)
Time_12 = x.strftime("%I") # 12 houres according time
print(Time_12)

PM = x.strftime("%p")
print(PM)

Secound = x.strftime("%S")
print(Secound)

import datetime

today = datetime.datetime.now()
print(today)

a = today.strftime("%Y")
print(a)
