mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


mystr = "banana"

for x in mystr:
  print(x)



class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    x = self.a
    self.a += 1
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)


def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)


def count_up_to(n):
  count = 1
  while count <= n:
    yield count
    count += 1

for num in count_up_to(5):
  print(num)



def large_sequence(n):
  for i in range(n):
    yield i

# This doesn't create a million numbers in memory
gen = large_sequence(1000000)
print(next(gen))
print(next(gen))
print(next(gen))

def simple_gen():
  yield "Emil"
  yield "Tobias"
  yield "Linus"

gen = simple_gen()
print(next(gen))
print(next(gen))
print(next(gen))

list_comp = [x * x for x in range(5)]
print(list_comp)

# Generator expression - creates a generator
gen_exp = (x * x for x in range(5))
print(gen_exp)
print(list(gen_exp))

total = sum(x * x for x in range(10))
print(total)

def fibonacci():
  a, b = 0, 1
  while True:
    yield a
    a, b = b, a + b

# Get first 100 Fibonacci numbers
gen = fibonacci()
for _ in range(100):
  print(next(gen))

def echo_generator():
  while True:
    received = yield
    print("Received:", received)

gen = echo_generator()
next(gen) # Prime the generator
gen.send("Hello")
gen.send("World")


def my_gen():
  try:
    yield 1
    yield 2
    yield 3
  finally:
    print("Generator closed")

gen = my_gen()
print(next(gen))
gen.close()



#my_example
#1
numbers = [10, 20, 30, 40]

myit = iter(numbers)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))


#2

class EvenNumbers:
    def __iter__(self):
        self.num = 2
        return self

    def __next__(self):
        if self.num <= 10:
            x = self.num
            self.num += 2
            return x
        else:
            raise StopIteration

myclass = EvenNumbers()

for x in myclass:
    print(x)


#3

def square_generator(n):
    for i in range(1, n + 1):
        yield i * i

for value in square_generator(5):
    print(value)



#4

gen_exp = (x + 5 for x in range(5))

print(next(gen_exp))
print(next(gen_exp))
print(next(gen_exp))

print(list(gen_exp))



#5
def countdown(start):
    while start > 0:
        yield start
        start -= 1

gen = countdown(5)

for num in gen:
    print(num)
