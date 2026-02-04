fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
  
#2
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#my_examples

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


letters = ["a", "b", "c", "d"]
for letter in letters:
    if letter == "c":
        break
    print(letter)


numbers = [10, 20, 30, 40, 50]
for n in numbers:
    print(n)
    if n == 30:
        break



animals = ["cat", "dog", "bird"]
for animal in animals:
    if animal == "dog":
        break
    print(animal)



for i in range(10):
    if i == 5:
        break
    print(i)
