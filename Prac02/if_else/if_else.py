a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#2
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#3
number = 7

if number % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")

#my_example

username = "Emil"

if len(username) > 0:
  print(f"Welcome, {username}!")
else:
  print("Error: Username cannot be empty")



activity = input("Куда вы идёте сегодня? (work/university/gym): ")

if activity == "work":
    print("Я одену офисную одежду")
elif activity == "university":
    print("Я одену более расслабленную одежду")
elif activity == "gym":
    print("Я одену спортивную одежду")
else:
    print("Я одену что-то удобное")


age = 16

if age >= 18:
    print("Access granted")
else:
    print("Access denied")


password = "12345"

if len(password) >= 8:
    print("Password is strong")
else:
    print("Password is too short")


x = 10
y = 25

if x < y:
    print("x is less than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is greater than y")
