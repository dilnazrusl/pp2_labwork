def myfunc(n):
  return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)

#my_examples

clothes = [("T-shirt", 5000), ("Jacket", 25000), ("Jeans", 15000), ("Hat", 3000)]

sorted_clothes = sorted(clothes, key=lambda x: x[1])

print(sorted_clothes)



foods = [("Burger", 550), ("Salad", 150), ("Pizza", 700), ("Apple", 80)]

sorted_foods = sorted(foods, key=lambda x: x[1])

print(sorted_foods)


clothes = ["coat", "t-shirt", "dress", "hoodie", "cap"]

sorted_clothes = sorted(clothes, key=lambda x: len(x))

print(sorted_clothes)


foods = ["pasta", "bread", "rice", "cake", "soup"]

sorted_foods = sorted(foods, key=lambda x: x[-1])

print(sorted_foods)


sizes = [34, 36, 38, 40, 42]

sorted_sizes = sorted(sizes, key=lambda x: abs(38 - x))

print(sorted_sizes)
