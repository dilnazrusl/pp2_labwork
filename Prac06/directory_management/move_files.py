import shutil
import os

# create directory
os.makedirs("backup", exist_ok=True)

# copy file
shutil.copy("sample.txt", "backup/sample_copy.txt")

print("File copied to backup folder")


import shutil
import os

# Example 1 - create directories
os.makedirs("source", exist_ok=True)
os.makedirs("destination", exist_ok=True)

# Example 2 - move file
with open("source/test.txt", "w") as f:
    f.write("Test file")

shutil.move("source/test.txt", "destination/test.txt")

# Example 3 - copy file
shutil.copy("file_handling/sample.txt", "destination/sample_copy.txt")

# Example 4 - list destination files
print(os.listdir("destination"))

# Example 5 - change directory
os.chdir("destination")
print("Current directory:", os.getcwd())



import shutil
import os
from pathlib import Path

# 1. Перемещение файла в другую папку
os.makedirs('archive', exist_ok=True)
with open('temp.txt', 'w') as f: f.write("test")
shutil.move('temp.txt', 'archive/temp.txt')

# 2. Поиск файлов по расширению (glob)
txt_files = list(Path('.').glob('*.txt'))
print("Text files found:", txt_files)

# 3. Смена рабочей директории
os.chdir('archive')
print("New directory:", os.getcwd())
os.chdir('..') # Возврат назад

# 4. Удаление дерева директорий (непустой папки)
shutil.rmtree('nested')

# 5. Копирование всей папки
if not os.path.exists('archive_copy'):
    shutil.copytree('archive', 'archive_copy')