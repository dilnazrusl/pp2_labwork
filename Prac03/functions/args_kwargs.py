def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_function("Emil", "Tobias", "Linus")


def my_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_function("Hello", "Emil", "Tobias", "Linus")

def my_function(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print(my_function(1, 2, 3))
print(my_function(10, 20, 30, 40))
print(my_function(5))

def my_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_function(3, 7, 2, 9, 1))

def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")


def my_function(**myvar):
  print("Type:", type(myvar))
  print("Name:", myvar["name"])
  print("Age:", myvar["age"])
  print("All data:", myvar)

my_function(name = "Tobias", age = 30, city = "Bergen")

def my_function(username, **details):
  print("Username:", username)
  print("Additional details:")
  for key, value in details.items():
    print(" ", key + ":", value)

my_function("emil123", age = 25, city = "Oslo", hobby = "coding")

def my_function(title, *args, **kwargs):
  print("Title:", title)
  print("Positional arguments:", args)
  print("Keyword arguments:", kwargs)

my_function("User Info", "Emil", "Tobias", age = 25, city = "Oslo")

def my_function(a, b, c):
  return a + b + c

numbers = [1, 2, 3]
result = my_function(*numbers) # Same as: my_function(1, 2, 3)
print(result)

def my_function(fname, lname):
  print("Hello", fname, lname)

person = {"fname": "Emil", "lname": "Refsnes"}
my_function(**person) # Same as: my_function(fname="Emil", lname="Refsnes")

def changecase(func):
  def myinner(*args, **kwargs):
    return func(*args, **kwargs).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))


#my_example

def last_added_item(*clothes):
    # Доступ по индексу, как в твоем примере с детьми
    print("The last item added to your cart is: " + clothes[-1])

last_added_item("T-shirt", "Jeans", "Sneakers", "Jacket")

def make_pizza(size, *toppings):
    print(f"Making a {size} inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza(12, "mushrooms", "peperoni", "extra cheese")

def describe_dish(name, **features):
    print("Dish name: " + name)
    for key, value in features.items():
        print(f"{key.capitalize()}: {value}")

describe_dish("Pasta Carbonara", calories=450, price="15$", spicy="No")

def process_order(customer, *items, **delivery_info):
    print(f"Customer: {customer}")
    print("Items ordered:", items)
    print("Delivery details:")
    for key, value in delivery_info.items():
        print(f"  {key}: {value}")

process_order("Alice", "Dress", "Handbag", address="123 Fashion St", express=True)

def create_outfit(brand, size, color):
    print(f"Added to outfit: {brand} sneakers, size {size}, color {color}")

sneakers_data = {"brand": "Nike", "size": 42, "color": "White"}

# Распаковка словаря: ключи станут именами аргументов
create_outfit(**sneakers_data)


