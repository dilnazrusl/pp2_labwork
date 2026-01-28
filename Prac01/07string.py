#Python - Slicing Strings

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])

b = "Hello, World!"
print(b[2:])

b = "Hello, World!"
print(b[-5:-2])


#Python - Modify Strings

a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"



a = "Hello, World!"
print(a.replace("H", "J"))


a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']



#myexamples

quote = "Python is amazing!"
print(quote[0:6])   # 'Python'
print(quote[7:9])   # 'is'
print(quote[-7:])   # 'amazing!'


name = "dIlNaZ"
print(name.upper())  # 'DILNAZ'
print(name.lower())  # 'dilnaz'
print(name.capitalize())  # 'Dilnaz'


text = "   Hello, Python!   "
print(text.strip())       # 'Hello, Python!'
print(text.lstrip())      # 'Hello, Python!   '
print(text.rstrip())      # '   Hello, Python!'


sentence = "I love Python, Java, and C++"
print(sentence.replace("Python", "JavaScript"))
print(sentence.split(", "))  # ['I love Python', 'Java', 'and C++']


word = "abcdefghij"
print(word[::2])   # каждый второй символ -> 'acegi'
print(word[::-1])  # перевернуть строку -> 'jihgfedcba'
