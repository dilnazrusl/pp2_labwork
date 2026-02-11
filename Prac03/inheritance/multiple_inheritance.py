class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()


#my_example

class Clothing:
    def __init__(self, fabric):
        self.fabric = fabric

class Tech:
    def __init__(self, battery_life):
        self.battery = battery_life

class SmartShirt(Clothing, Tech):
    def __init__(self, fabric, battery, color):
        Clothing.__init__(self, fabric)
        Tech.__init__(self, battery)
        self.color = color

    def show_specs(self):
        print(f"Smart Shirt: {self.color}, {self.fabric}, Battery: {self.battery}h")

shirt = SmartShirt("Cotton", 24, "Black")
shirt.show_specs()


class Dish:
    def __init__(self, dish_name):
        self.dish_name = dish_name

class Delivery:
    def __init__(self, address):
        self.address = address

class TakeAwayOrder(Dish, Delivery):
    def __init__(self, name, address, time):
        Dish.__init__(self, name)
        Delivery.__init__(self, address)
        self.time = time

    def print_ticket(self):
        print(f"Order: {self.dish_name} to {self.address} at {self.time}")

order = TakeAwayOrder("Pizza Margherita", "123 Maple St", "18:30")
order.print_ticket()


class Footwear:
    def __init__(self, size):
        self.size = size

class WinterGear:
    def __init__(self, min_temp):
        self.min_temp = min_temp

class WinterSneakers(Footwear, WinterGear):
    def __init__(self, size, temp, brand):
        Footwear.__init__(self, size)
        WinterGear.__init__(self, temp)
        self.brand = brand

    def check_comfort(self):
        print(f"{self.brand} shoes, size {self.size}. Good for {self.min_temp}°C")

my_boots = WinterSneakers(42, -20, "Columbia")
my_boots.check_comfort()

class Dessert:
    def __init__(self, sugar_content):
        self.sugar = sugar_content

class Vegan:
    def __init__(self, is_dairy_free):
        self.dairy_free = is_dairy_free

class VeganCake(Dessert, Vegan):
    def __init__(self, sugar, dairy_free, flavor):
        Dessert.__init__(self, sugar)
        Vegan.__init__(self, dairy_free)
        self.flavor = flavor

    def info(self):
        print(f"{self.flavor} cake. Sugar: {self.sugar}g. Dairy-free: {self.dairy_free}")

cake = VeganCake(15, True, "Vanilla")
cake.info()

class Uniform:
    def __init__(self, u_type):
        self.u_type = u_type

class Brand:
    def __init__(self, company_name):
        self.company = company_name

class StaffJacket(Uniform, Brand):
    def __init__(self, u_type, company, employee_name):
        Uniform.__init__(self, u_type)
        Brand.__init__(self, company)
        self.employee = employee_name

    def display(self):
        print(f"Employee: {self.employee} | {self.company} {self.u_type}")

worker = StaffJacket("Windbreaker", "Starbucks", "John")
worker.display()

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

    
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2016
    
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Dilnaz", "Rustam", 2016)