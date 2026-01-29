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

#3
colors = ["red", "blue", "green", "yellow"]
for color in colors:
    if color == "green":
        continue
    print(color)


#4

nums = range(1, 10)
for i in nums:
    if i % 2 == 0:
        continue
    print(i)


#5
letters = ["a", "b", "c", "d"]
for letter in letters:
    if letter == "b" or letter == "d":
        continue
    print(letter)

