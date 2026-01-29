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
print(quote[0:6]) 
print(quote[7:9])   
print(quote[-7:])   


name = "dIlNaZ"
print(name.upper()) 
print(name.lower())  
print(name.capitalize())  


text = "   Hello, Python!   "
print(text.strip())      
print(text.lstrip())      
print(text.rstrip())      


sentence = "I love Python, Java, and C++"
print(sentence.replace("Python", "JavaScript"))
print(sentence.split(", ")) 


word = "abcdefghij"
print(word[::2])  
print(word[::-1])  
