ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = filter(myFunc, ages)

for x in adults:
  print(x)


#my_example

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

evens = filter(lambda x: x % 2 == 0, numbers)

for n in evens:
    print(n)


numbers = [10, 15, 20, 25, 30, 35]

odds = filter(lambda x: x % 2 != 0, numbers)

for n in odds:
    print(n)


words = ["cat", "elephant", "dog", "tiger", "hi"]

long_words = filter(lambda w: len(w) > 4, words)

for word in long_words:
    print(word)


nums = [-10, -5, 0, 3, 8, -2, 7]

positive = filter(lambda x: x > 0, nums)

for n in positive:
    print(n)


names = ["Alice", "Bob", "Anna", "Mike", "Alex"]

a_names = filter(lambda name: name.startswith("A"), names)

for name in a_names:
    print(name)


numbers = list(range(1, 51))

special = filter(lambda x: x % 3 == 0 and x % 5 == 0, numbers)

for n in special:
    print(n)
