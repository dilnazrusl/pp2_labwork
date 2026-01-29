
#0_01
print(bool("Hello"))
print(bool(15))

#0_02
x = "Hello"
y = 15

print(bool(x))
print(bool(y))

#0_03
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


#0_03
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


#0_04
def myFunction() :
  return True

print(myFunction())


#0_05
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")



#0_06
x = 200
print(isinstance(x, int))




#1
print(bool("Python"))
print(bool(0))

a = ""
b = 42

print(bool(a))
print(bool(b))

#2
class Example:
    def __len__(self):
        return 5

obj = Example()
print(bool(obj))  # True, так как __len__ возвращает 5

class EmptyExample:
    def __len__(self):
        return 0

empty_obj = EmptyExample()
print(bool(empty_obj))  # False, так как __len__ возвращает 0


#3
x = 3.14
y = "Hello"

print(isinstance(x, float))  # True
print(isinstance(y, str))    # True
print(isinstance(y, int))    # False

#4
def is_even(number):
    return number % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False

if is_even(8):
    print("Even")
else:
    print("Odd")


#5
a = None
b = 5
c = ""

print(bool(a))
print(bool(b))
print(bool(c))

if b and not a:
    print("b is True and a is False")



#0_01
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

#0_02
print(10 + 5)


#1_01
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)


#1_02
x = 12
y = 5
print(x / y)





#1
x1 = 19
y1 = 4
print(x1 // y1)



#2
val = 29
num = 5
print(val // num)
print(val % num)



#2_01
numbers = [1, 2, 3, 4, 5]
count = len(numbers)
if count > 3:
    print(f"List has {count} elements")

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

