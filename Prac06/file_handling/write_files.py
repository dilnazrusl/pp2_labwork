# write mode
# Writing to a file

with open("sample.txt", "w") as f:
    f.write("10\n")
    f.write("25\n")
    f.write("30\n")
    f.write("15\n")

print("File written successfully")

# Example 1 - write new file
file = open("new_file.txt", "w")
file.write("This is a new file\n")
file.close()


# Example 2 - write multiple lines
file = open("new_file.txt", "w")
file.write("Line 1\n")
file.write("Line 2\n")
file.close()


# Example 3 - append text
file = open("new_file.txt", "a")
file.write("Appended line\n")
file.close()


# Example 4 - write using with
with open("with_file.txt", "w") as file:
    file.write("Using context manager\n")


# Example 5 - create file using x mode
try:
    file = open("created_file.txt", "x")
    file.write("File created using x mode")
    file.close()
except FileExistsError:
    print("File already exists")


# 1. Запись в новый файл (режим 'w' перезаписывает)
with open('output.txt', 'w') as f:
    f.write("This is a new file.\n")

# 2. Добавление текста в конец (режим 'a')
with open('output.txt', 'a') as f:
    f.write("Adding a new line here.\n")

# 3. Запись списка строк через writelines()
lines = ["Line A\n", "Line B\n", "Line C\n"]
with open('output.txt', 'a') as f:
    f.writelines(lines)

# 4. Использование режима 'x' (создать, если не существует)
try:
    with open('exclusive.txt', 'x') as f:
        f.write("Unique file content.")
except FileExistsError:
    print("File already exists!")

# 5. Запись данных с использованием print(file=...)
with open('output.txt', 'a') as f:
    print("Formatted line via print", file=f)