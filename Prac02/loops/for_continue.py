fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


#2
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n == 3:
        continue
    print(n)

#my_examples

colors = ["red", "blue", "green", "yellow"]
for color in colors:
    if color == "green":
        continue
    print(color)



nums = range(1, 10)
for i in nums:
    if i % 2 == 0:
        continue
    print(i)



letters = ["a", "b", "c", "d"]
for letter in letters:
    if letter == "b" or letter == "d":
        continue
    print(letter)


for i in range(6):
    if i == 4:
        continue
    print(i)

numbers = [3, -1, 5, -2, 7]

for n in numbers:
    if n < 0:
        continue
    print(n)


animals = ["cat", "dog", "fish"]

for animal in animals:
    if animal == "dog":
        continue
    print(animal)
