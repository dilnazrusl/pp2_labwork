#Python Variables

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


#Many Values to Multiple Variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


x = y = z = "Orange"
print(x)
print(y)
print(z)


fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


#Python - Output Variables
x = "Python is awesome"
print(x)


x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = 5
y = 10
print(x + y)

x = 5
y = "John"
print(x, y)

#Python - Global Variables

x = "awesome"
def myfunc():
  print("Python is " + x)
myfunc()


x = "awesome"
def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x)


x = "awesome"
def myfunc():
  global x
  x = "fantastic"
myfunc()
print("Python is " + x)



#myexamples

player = "Alex"
score = 0

score = score + 10
print(player, "score:", score)


hero = "Wizard"
hero = "Knight"

print("Hero is:", hero)


code = [7, 2, 9]
a, b, c = code

print(a)
print(b)
print(c)


power = 100

def boost():
    global power
    power = power + 50

boost()
print("Power level:", power)



name = "Diana"
language = "Python"

message = "Hello " + name + ", welcome to " + language
print(message)
