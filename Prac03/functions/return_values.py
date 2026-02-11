def myfunc():
  x = 300
  print(x)

myfunc()

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()


x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())


x = "global"

def outer():
  x = "enclosing"
  def inner():
    x = "local"
    print("Inner:", x)
  inner()
  print("Outer:", x)

outer()
print("Global:", x)


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())


def changecase(func):
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Hello Sally"

@changecase
def otherfunction():
  return "I am speed!"

print(myfunction())
print(otherfunction())


def changecase(func):
  def myinner(x):
    return func(x).upper()
  return myinner

@changecase
def myfunction(nam):
  return "Hello " + nam

print(myfunction("John"))

def myfunction():
  return "Have a great day!"

print(myfunction.__name__)



#my_examples

def daily_special():
    return "Today's special is Grilled Salmon"

suggestion = daily_special()
print(suggestion)


def check_sugar(grams):
    if grams > 10:
        return "Sweet"
    return "Healthy"

print(check_sugar(2))     # Healthy
result1 = check_sugar(15)
result2 = check_sugar(5)
print(result1)            # Sweet
print(result2)            # Healthy


def get_most_expensive(prices):
    highest = prices[0]
    for price in prices:
        if price > highest:
            highest = price
    return highest

clothing_prices = [45, 120, 89, 250, 30]
print("Most expensive item costs:", get_most_expensive(clothing_prices))


def swap_accessories(person1_item, person2_item):
    return person2_item, person1_item

my_hat = "Red Cap"
your_hat = "Blue Beanie"

my_hat, your_hat = swap_accessories(my_hat, your_hat)
print("I now have:", my_hat)
print("You now have:", your_hat)


def apply_discount(price, discount_percent):
    final_price = price - (price * discount_percent / 100)
    return final_price

jacket_price = 100
sale_price = apply_discount(jacket_price, 20) # 20% скидка

print(f"Old price: {jacket_price}, New price: {sale_price}")


