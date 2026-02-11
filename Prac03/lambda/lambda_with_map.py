def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

#my_example

clothes = ["t-shirt", "JACKET", "jeans", "socks"]
# Метод capitalize() сделает первую букву заглавной
formatted_clothes = list(map(lambda item: item.capitalize(), clothes))

print(formatted_clothes) # ['T-shirt', 'Jacket', 'Jeans', 'Socks']

sizes = ["S", "M", "L", "XL"]
# Конкатенация строк внутри map
labeled_sizes = list(map(lambda s: "Size: " + s, sizes))

print(labeled_sizes) # ['Size: S', 'Size: M', 'Size: L', 'Size: XL']


items = ["Sneakers", "Belt", "Hoodie", "Scarf"]
# Получаем количество символов в каждом слове
name_lengths = list(map(lambda x: len(x), items))

print(name_lengths) # [8, 4, 6, 5]


clothing_items = ["Jacket", "Trousers", "Cap", "Gloves"]
# Соединяем цвет и тип одежды в одну строку
matching_outfit = list(map(lambda item: "Vintage White " + item, clothing_items))

print(matching_outfit) 
# ['Vintage White Jacket', 'Vintage White Trousers', 'Vintage White Cap', 'Vintage White Gloves']

items = ["Hoodie", "Suit", "T-shirt", "Tuxedo"]
# Если одежда официальная (Suit/Tuxedo), ставим 'Formal', иначе 'Casual'
categorized_items = list(map(lambda x: x + " (Formal)" if x == "Suit" or x == "Tuxedo" else x + " (Casual)", items))

print(categorized_items)
# ['Hoodie (Casual)', 'Suit (Formal)', 'T-shirt (Casual)', 'Tuxedo (Formal)']

