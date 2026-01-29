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

#3
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#4
letters = ["a", "b", "c", "d"]
for letter in letters:
    if letter == "c":
        break
    print(letter)

#5
numbers = [10, 20, 30, 40, 50]
for n in numbers:
    print(n)
    if n == 30:
        break
