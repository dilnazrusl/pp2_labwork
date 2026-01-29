a = 5
b = 2
if a > b: print("a is greater than b")

#2
a = 2
b = 330
print("A") if a > b else print("B")

#3
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#4
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


#5
x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#6
username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)


#7
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#8
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#9
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")
  
#10
  age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#11
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

#12
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

#13
  score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

#14
  x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#15
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#16
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#17
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")


#18
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

#19
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet
