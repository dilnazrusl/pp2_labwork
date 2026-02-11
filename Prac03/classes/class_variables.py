#my_examples



class Student:
    university = "KBTU"   # class variable (общая для всех)

    def __init__(self, name):
        self.name = name  # instance variable (у каждого своя)

s1 = Student("Dilnaz")
s2 = Student("Aruzhan")

print(s1.university)
print(s2.university)
print(s1.name)
print(s2.name)


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("Toyota", 2020)

print(c1.year)

c1.year = 2024   # изменяем свойство
print(c1.year)


class Phone:
    country = "USA"

    def __init__(self, model):
        self.model = model

p1 = Phone("iPhone")
p2 = Phone("Samsung")

Phone.country = "Japan"   # меняем для всех

print(p1.country)
print(p2.country)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Dilnaz", 20)

print(p1.age)

del p1.age   # удаляем age

print(p1.name)


class Book:
    def __init__(self, title):
        self.title = title

b1 = Book("Python Basics")

print(b1.title)

del b1   # удаляем объект

# print(b1.title)  ← будет ошибка
