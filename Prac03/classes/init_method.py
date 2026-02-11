class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)


#my_example

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("Dilnaz", 20)

print(p1.name)
print(p1.age)


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

c1 = Car("Toyota", "Camry", 2022)

print(c1.brand)
print(c1.model)
print(c1.year)

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

b1 = Book("1984", "George Orwell", 328)

print(b1.title)
print(b1.author)
print(b1.pages)

class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories

f1 = Food("Burger", 550)
f2 = Food("Salad", 150)

print(f1.name, f1.calories)
print(f2.name, f2.calories)

class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

l1 = Laptop("HP", 16, 512)

print(l1.brand)
print(l1.ram)
print(l1.storage)
