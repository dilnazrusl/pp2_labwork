#my_example

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def describe(self):
        print(f"This is {self.name} and it costs ${self.price}")

class Soup(Dish):
    def __init__(self, name, price, temperature):
        super().__init__(name, price)
        self.temp = temperature

    # Переопределение (Overriding)
    def describe(self):
        super().describe() # Вызываем старую логику
        print(f"Careful, it is served {self.temp}!")

my_soup = Soup("Borscht", 12, "hot")
my_soup.describe()

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_total_price(self):
        return self.price

class SaleItem(Item):
    def __init__(self, name, price, discount):
        super().__init__(name, price)
        self.discount = discount

    # Переопределение метода расчета цены
    def get_total_price(self):
        return self.price - self.discount

jacket = SaleItem("Leather Jacket", 200, 50)
print(f"Final price: {jacket.get_total_price()}") # Выведет 150

class Guest:
    def __init__(self, name):
        self.name = name

    def welcome(self):
        print("Hello", self.name)

class VIPGuest(Guest):
    def __init__(self, name, table_number):
        super().__init__(name)
        self.table = table_number

    # Полное переопределение метода welcome
    def welcome(self):
        print(f"Welcome, Mr/Ms {self.name}! Your VIP table #{self.table} is ready.")

guest = VIPGuest("Alex", 5)
guest.welcome()

class Coffee:
    def __init__(self, size):
        self.size = size

    def make(self):
        print(f"Making a {self.size} cup of black coffee.")

class Latte(Coffee):
    def __init__(self, size, milk_type):
        super().__init__(size)
        self.milk = milk_type

    def make(self):
        # Используем базу родителя, но дополняем её
        super().make()
        print(f"Adding steamed {self.milk} milk for your latte.")

order = Latte("Large", "Oat")
order.make()


class Shoes:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def info(self):
        print(f"Brand: {self.brand}, Size: {self.size}")

class RunningShoes(Shoes):
    def __init__(self, brand, size, weight):
        super().__init__(brand, size)
        self.weight = weight

    # Переопределяем info, чтобы добавить вес кроссовок
    def info(self):
        super().info()
        print(f"Type: Lightweight Running, Weight: {self.weight}g")

pro_shoes = RunningShoes("Adidas", 42, 250)
pro_shoes.info()


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

  def welcome(self):
    print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)

    