from functools import reduce

numbers = [10, 25, 30, 15, 40, 5]

# map example
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers:", squared)

# filter example
greater_than_20 = list(filter(lambda x: x > 20, numbers))
print("Numbers > 20:", greater_than_20)

# reduce example
total = reduce(lambda x, y: x + y, numbers)
print("Sum using reduce:", total)


from functools import reduce

numbers = [1,2,3,4,5,6]

# Example 1 - map
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Example 2 - filter
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)

# Example 3 - reduce (sum)
total = reduce(lambda a,b: a+b, numbers)
print(total)

# Example 4 - reduce (multiplication)
product = reduce(lambda a,b: a*b, numbers)
print(product)

# Example 5 - combine map and filter
result = list(map(lambda x: x*2, filter(lambda x: x>3, numbers)))
print(result)
