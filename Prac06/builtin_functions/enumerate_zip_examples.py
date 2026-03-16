names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# enumerate example
for index, name in enumerate(names):
    print(index, name)

# zip example
for name, score in zip(names, scores):
    print(name, score)

# built in functions
numbers = [10, 25, 30, 15, 40, 5]

print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))

# type conversion
num_str = "100"
num_int = int(num_str)

print("Converted type:", type(num_int))


names = ["Alice", "Bob", "Charlie"]
scores = [85, 90, 78]

# Example 1 - enumerate
for index, name in enumerate(names):
    print(index, name)

# Example 2 - enumerate starting from 1
for index, name in enumerate(names, start=1):
    print(index, name)

# Example 3 - zip
paired = list(zip(names, scores))
print(paired)

# Example 4 - iterate zip
for name, score in zip(names, scores):
    print(name, score)

# Example 5 - sorted
sorted_scores = sorted(scores)
print(sorted_scores)
