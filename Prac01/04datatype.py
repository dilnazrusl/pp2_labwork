#Python Data Types
#Getting the Data Type

x = 5
print(type(x))

x = 1j
print(x)
#display the data type of x:
print(type(x)) 

x = ["apple", "banana", "cherry"]
print(type(x))

x = ("apple", "banana", "cherry")
print(type(x))

x = range(6)
print(type(x))

x = {"name" : "John", "age" : 36}
print(type(x))

x = {"apple", "banana", "cherry"}
print(type(x))

x = frozenset({"apple", "banana", "cherry"})
print(type(x))

x = b"Hello"
print(type(x))

x = bytearray(5)
print(type(x))

x = memoryview(bytes(5))
print(type(x))

x = None
print(type(x))
# #print(None == 0)     # False
# print(None == "")    # False
# print(None == False) # False



#myexample

x = 42
print(x)
print(type(x))

y = 3.14
print(y)
print(type(y))



text = "Python"
is_fun = True

print(text)
print(type(text))

print(is_fun)
print(type(is_fun))



items_list = ["pen", "book", "phone"]
items_tuple = ("pen", "book", "phone")

print(type(items_list))
print(type(items_tuple))



student = {
    "name": "Anna",
    "grade": 90
}

subjects = {"Math", "IT", "Physics"}

print(type(student))
print(type(subjects))


result = None

print(result)
print(type(result))
