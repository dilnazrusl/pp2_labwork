# Reading files

with open("sample.txt", "r") as f:
    content = f.read()
    print("File content:")
    print(content)

with open("sample.txt", "r") as f:
    print("Read line by line:")
    print(f.readline())
    print(f.readline())

with open("sample.txt", "r") as f:
    lines = f.readlines()
    print("Readlines result:")
    print(lines)


# 1. Чтение всего файла сразу через read()
with open('sample2.txt', 'r') as f:
    print("Example 1:\n", f.read())

# 2. Построчное чтение через readline()
with open('sample2.txt', 'r') as f:
    print("Example 2 (First line):", f.readline().strip())

# 3. Чтение всех строк в список через readlines()
with open('sample2.txt', 'r') as f:
    lines = f.readlines()
    print("Example 3 (List of lines):", lines)

# 4. Итерация по объекту файла (самый эффективный способ)
print("Example 4 (Iteration):")
with open('sample2.txt', 'r') as f:
    for line in f:
        print("- " + line.strip())

# 5. Чтение определенного количества символов
with open('sample2.txt', 'r') as f:
    print("Example 5 (First 10 chars):", f.read(10))