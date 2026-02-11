def my_function():
  print("Hello from a function")


def my_function():
  print("Hello from a function")

my_function()

def my_function():
  print("Hello from a function")

my_function()
my_function()
my_function()

temp1 = 77
celsius1 = (temp1 - 32) * 5 / 9
print(celsius1)

temp2 = 95
celsius2 = (temp2 - 32) * 5 / 9
print(celsius2)

temp3 = 50
celsius3 = (temp3 - 32) * 5 / 9
print(celsius3)


def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(95))
print(fahrenheit_to_celsius(50))



def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)


def get_greeting():
  return "Hello from a function"

print(get_greeting())

def my_function():
  pass



#my_example

def shout(text):
    return text.upper() + "!!!"

print(shout("hello"))
print(shout("Dilnaz is cool"))


def secret_code(word):
    return word[::-1]

print(secret_code("Dilnaz"))
print(secret_code("12345"))


def is_lucky(number):
    total = sum(int(d) for d in str(number))
    return total % 2 == 0

print(is_lucky(123))   # False
print(is_lucky(246))   # True



def calculate(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    else:
        return "Unknown operation"

print(calculate(5, 3, "+"))
print(calculate(10, 4, "-"))
print(calculate(6, 7, "*"))


def  Atyrau():
  print("Hello from Atyrau")

Atyrau()
