class Parent:
  def __init__(self, txt):
    self.message = txt

  def printmessage(self):
    print(self.message)

class Child(Parent):
  def __init__(self, txt):
    super().__init__(txt)

x = Child("Hello, and welcome!")

x.printmessage()

#my_example

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_brand(self):
        print("Brand:", self.brand)

class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand)
        self.model = model

    def show_info(self):
        super().show_brand()  # вызываем метод родителя
        print("Model:", self.model)

c1 = Car("Toyota", "Corolla")
c1.show_info()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name, "makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def speak(self):
        super().speak()   # вызываем родительский метод
        print(self.name, "barks")

d1 = Dog("luki", "Labrador")
d1.speak()


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        print("Employee:", self.name, "Salary:", self.salary)

class Manager(Employee):
    def __init__(self, name, salary, dept):
        super().__init__(name, salary)
        self.department = dept

    def show(self):
        super().show()
        print("Department:", self.department)

m1 = Manager("Dilnaz", 5000, "IT")
m1.show()


class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def full_name(self):
        return self.fname + " " + self.lname

class Student(Person):
    def __init__(self, fname, lname, major):
        super().__init__(fname, lname)
        self.major = major

    def introduce(self):
        print("Hello, I'm", super().full_name(), "and I study", self.major)

s1 = Student("Dilnaz", "Ruslanova", "IT")
s1.introduce()


class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        parent_area = super().area()  # вызов родителя (хотя он 0)
        return self.length * self.width + parent_area

r1 = Rectangle(5, 3)
print(r1.area())

