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
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def display(self):
        print(f"Brand: {self.brand}, Size: {self.size}")

# Дочерний класс (ничего своего не добавляет)
class TShirt(Clothing):
    pass

item = TShirt("Nike", "L")
item.display()

class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

    def info(self):
        print(f"Item: {self.name}, Calories: {self.calories} kcal")

class Fruit(Food):
    pass

apple = Fruit("Green Apple", 52)
apple.info()


class Appliance:
    def __init__(self, model):
        self.model = model

    def turn_on(self):
        print(f"The {self.model} is now working.")

class Toaster(Appliance):
    pass

my_toaster = Toaster("Bosch T100")
my_toaster.turn_on()


class Footwear:
    def __init__(self, material, color):
        self.material = material
        self.color = color

    def show_details(self):
        print(f"Material: {self.material}, Color: {self.color}")

class Sneakers(Footwear):
    pass

my_shoes = Sneakers("Leather", "White")
my_shoes.show_details()

class Recipe:
    def __init__(self, main_ingredient, time):
        self.ingredient = main_ingredient
        self.time = time

    def cook(self):
        print(f"Cooking with {self.ingredient}. Ready in {self.time} mins.")

class Dessert(Recipe):
    pass

cake = Dessert("Chocolate", 45)
cake.cook()

