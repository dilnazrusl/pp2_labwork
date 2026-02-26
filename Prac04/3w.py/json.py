import json
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'
# parse x:
y = json.loads(x)
# the result is a Python dictionary:
print(y["age"])



import json
# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}
# convert into JSON:
y = json.dumps(x)
# the result is a JSON string:
print(y)


import json
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


import json
x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(x))

json.dumps(x, indent=4)

json.dumps(x, indent=4, separators=(". ", " = "))

json.dumps(x, indent=4, sort_keys=True)



#my example

import json

# JSON string
x = '{ "student":"dilnaz", "grade":100, "city":"Almaty"}'

# parse JSON
y = json.loads(x)

# result is Python dictionary
print(y["student"])
print(y["grade"])


#2

import json

# Python dictionary
x = {
    "product": "Laptop",
    "price": 450000,
    "available": True
}

# convert to JSON string
y = json.dumps(x)

print(y)


#3
import json

x = {
    "name": "Dias",
    "age": 20,
    "country": "Kazakhstan"
}

print(json.dumps(x, indent=4))
print(json.dumps(x, indent=4, sort_keys=True))

#4

import json

data = {
    "name": "Aigerim",
    "age": 19,
    "major": "IT"
}

with open("student.json", "w") as file:
    json.dump(data, file)

#5
import json

with open("sample-data.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"]) 
