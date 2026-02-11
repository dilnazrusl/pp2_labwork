x = lambda a : a + 10
print(x(5))


x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

def myfunc(n):
  return lambda a : a * n

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))

numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)

students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)


words = ["apple", "pie", "banana", "cherry"]
sorted_words = sorted(words, key=lambda x: len(x))
print(sorted_words)

#my_examples

add_delivery = lambda price : price + 5
print(add_delivery(20)) # Бургер за 20 + 5 доставка

total_calories = lambda portions, cal_per_one : portions * cal_per_one
print(total_calories(3, 250)) # 3 порции по 250 калорий

def discount_factory(multiplier):
    return lambda price : price * multiplier

# Создаем функцию для скидки 10% (умножаем на 0.9)
standard_discount = discount_factory(0.9)
# Создаем функцию для скидки 30% (умножаем на 0.7)
vip_discount = discount_factory(0.7)

print(standard_discount(100)) # Куртка за 100 станет 90
print(vip_discount(100))      # Куртка за 100 станет 70

prices = [5, 12, 8, 20, 7, 15]
# Оставляем только бюджетные варианты (cheap)
budget_meals = list(filter(lambda p: p < 10, prices))
print(budget_meals) # [5, 8, 7]

t_shirts = [("Blue", 52), ("Red", 48), ("Green", 56), ("White", 50)]
# Сортируем по второму элементу кортежа (размеру)
sorted_shirts = sorted(t_shirts, key=lambda shirt: shirt[1])

print(sorted_shirts) 
# Результат: [('Red', 48), ('White', 50), ('Blue', 52), ('Green', 56)]

