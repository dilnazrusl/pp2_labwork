import shutil
import os

# Copy file
shutil.copy("sample.txt", "backup_sample.txt")
print("File copied")

# Delete file safely
if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
    print("Backup file deleted")
else:
    print("File does not exist")

import shutil
import os


import shutil
import os

# Example 1 - copy file
shutil.copy("sample.txt", "copy_sample.txt")

# Example 2 - create backup
shutil.copy("sample.txt", "backup_sample.txt")

# Example 3 - copy with metadata
shutil.copy2("sample.txt", "copy2_sample.txt")

# Example 4 - delete file safely
if os.path.exists("copy_sample.txt"):
    os.remove("copy_sample.txt")

# Example 5 - check file exists
if os.path.exists("backup_sample.txt"):
    print("Backup file exists")


# 1. Копирование файла
shutil.copy('sample.txt', 'sample_backup.txt')

# 2. Копирование с сохранением метаданных
shutil.copy2('sample.txt', 'sample_meta_backup.txt')

# 3. Проверка существования перед удалением
if os.path.exists('exclusive.txt'):
    os.remove('exclusive.txt')

# 4. Переименование файла
if os.path.exists('sample_meta_backup.txt'):
    os.rename('sample_meta_backup.txt', 'renamed_backup.txt')

# 5. Безопасное удаление (обработка ошибки)
try:
    os.remove('non_existent.txt')
except FileNotFoundError:
    print("File not found, nothing to delete.")

