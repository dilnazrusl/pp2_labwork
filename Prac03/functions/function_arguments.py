def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")



def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")



def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")


def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")


def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)


def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)



def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)


def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])


def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

def my_function(name, /):
  print("Hello", name)

my_function("Emil")

def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

def my_function(name):
  print("Hello", name)

my_function("Emil")

def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)



#my_example

def study_course(subject):
    print("Изучаю курс по: " + subject)

study_course("Python")
study_course("Data Science")
study_course("AI")


def order_status(item, status = "в очереди"):
    print(f"Заказ '{item}' сейчас имеет статус: {status}")

order_status("Кофе", "готов")
order_status("Пицца") # Использует значение по умолчанию
order_status("Чай", "готовится")

def create_hero(level, hero_class, name):
    print(f"Создан герой {name}: {hero_class} {level} уровня.")

# Порядок изменен, но Python поймет, что куда подставить
create_hero(name="Арагорн", level=80, hero_class="Воин")

def show_tasks(tasks):
    print("Ваш список дел на сегодня:")
    for task in tasks:
        print("- " + task)

to_do = ["Купить хлеб", "Помыть машину", "Позвонить маме"]
show_tasks(to_do)

def get_player_position():
    x = 100
    y = 250
    return x, y

pos_x, pos_y = get_player_position()
print("Координата X:", pos_x)
print("Координата Y:", pos_y)

