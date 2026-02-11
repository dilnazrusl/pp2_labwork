class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

p1 = MyClass()
p2 = MyClass()
p3 = MyClass()

print(p1.x)
print(p2.x)
print(p3.x)

class Person:
  pass


#my_examples
class student:
    name="Dilnaz"
    age=20
    major="information tchnolagy"

x=student()
print(x.name)
del x
x=student()
print(x.name)
print(x.age)
print(x.major)

class Book:
    title = "Harry Potter"
    author = "J.K. Rowling"

b1 = Book()
print(b1.title)
print(b1.author)


class Car:
    brand = "Toyota"
    year = 2023

c1 = Car()
c2 = Car()

print(c1.brand)
print(c2.year)


class Phone:
    model = "iPhone"
    storage = 128

p1 = Phone()
print(p1.model)

del p1

p1 = Phone()
print(p1.storage)


class University:
    name = "KBTU"
    city = "Almaty"

u1 = University()
u2 = University()

print(u1.name)
print(u2.city)


class Food:
    name = "Pizza"
    calories = 700

f1 = Food()
f2 = Food()
f3 = Food()

print(f1.name)
print(f2.calories)
print(f3.name)
