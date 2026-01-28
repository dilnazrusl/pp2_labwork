#Python Casting

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

#Python Strings
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = "Hello, World!"
print(a[1])

for x in "banana":
  print(x)


a = "Hello, World!"
print(len(a))

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")


txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

#myexamples

score_str = "50"
bonus_str = "20"

score = int(score_str)
bonus = int(bonus_str)

total = score + bonus
print("Total points:", total)
print("Type of total:", type(total))


a = int(10)
b = float(5.5)
c = complex(2, 3)

print("a + b + c =", a + b + c)
print("Type of result:", type(a + b + c))


age = input("Enter your age: ")  # input возвращает строку
age = int(age)                    # превращаем в число
next_year = age + 1
print("Next year you will be:", next_year)



length_str = "5.7"
width_str = "3.2"

length = float(length_str)
width = float(width_str)
area = length * width

print("Area of rectangle:", area)
print("Type of area:", type(area))



cash = int(100)       # наличные
gift_card = float(25.5) # подарочная карта
crypto = complex(0, 10) # криптовалюта в виде imaginary

total = cash + gift_card + crypto
print("Total money:", total)
print("Type of total:", type(total))


atoms = int(12)
temperature = float(36.6)
electric_field = complex(0, 5)

result = atoms + temperature + electric_field
print("Experiment result:", result)
print("Type of result:", type(result))
