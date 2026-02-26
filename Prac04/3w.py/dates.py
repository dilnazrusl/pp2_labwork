import datetime

x = datetime.datetime.now()
print(x)


import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))



import datetime

x = datetime.datetime(2020, 5, 17)

print(x)


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%a"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%A"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%w"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%d"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%Y"))


import datetime

x = datetime.datetime.now()

print(x.strftime("%f"))

import datetime

x = datetime.datetime.now()

print(x.strftime("%c"))


#my_example

import datetime

x = datetime.datetime(2024, 12, 25, 18, 30)

print(x)

#2

import datetime

x = datetime.datetime.now()

print(x.strftime("%d/%m/%Y"))
print(x.strftime("%H:%M"))

#3
import datetime

date1 = datetime.datetime(2025, 1, 1)
date2 = datetime.datetime.now()

difference = date2 - date1

print("Days passed:", difference.days)

#4
import datetime

x = datetime.datetime.now()

print(x.time())
print(x.strftime("%H:%M:%S"))

#5
import datetime

utc_now = datetime.datetime.now(datetime.timezone.utc)

print("UTC time:", utc_now)

local_time = utc_now.astimezone()

print("Local time:", local_time)