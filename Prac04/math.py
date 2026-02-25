x = min(5, 10, 25)
y = max(5, 10, 25)
print(x)
print(y)


x = abs(-7.25)
print(x)


x = pow(4, 3)
print(x)


import math
x = math.sqrt(64)
print(x)


import math
x = math.ceil(1.4)
y = math.floor(1.4)
print(x) # returns 2
print(y) # returns 1


import math
x = math.pi
print(x)

#my example

x = min(12, 7, 25, 3)
y = max(12, 7, 25, 3)
z = round(5.6789, 2)

print(x)
print(y)
print(z)

#2
a = abs(-15)
b = pow(2, 5)

print(a)
print(b)

#3
import math

x = math.sqrt(81)
y = math.pi
z = math.e

print(x)
print(y)
print(z)

#4
import math

a = math.ceil(4.3)
b = math.floor(4.9)
c = math.sin(math.pi / 2)
d = math.cos(0)

print(a)
print(b)
print(c)
print(d)

#5
import random

print(random.random())       
print(random.randint(1, 10)) 
fruits = ["apple", "banana", "cherry"]
print(random.choice(fruits))  
random.shuffle(fruits)
print(fruits)                 