#3_01
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#3_02
x = 5

print(1 < x < 10)

print(1 < x and x < 10)

#4_01
x = 5

print(x > 0 and x < 10)

#4_02
x = 5

print(x < 5 or x > 10)

#4_03
x = 5

print(not(x > 3 and x < 10))


#5_01
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#5_02
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

#5_03
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#6_01
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#6_02
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

#6_03
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)


