import os

# Current directory
print("Current directory:", os.getcwd())

# Create directories
os.makedirs("test_folder/subfolder", exist_ok=True)

print("Directories created")

# List files
print("Files in directory:")
print(os.listdir())


import os

# Example 1 - create directory
os.mkdir("test_folder")

# Example 2 - create nested directories
os.makedirs("parent/child/grandchild", exist_ok=True)

# Example 3 - list files and folders
files = os.listdir(".")
print(files)

# Example 4 - get current working directory
print(os.getcwd())

# Example 5 - remove directory
if os.path.exists("test_folder"):
    os.rmdir("test_folder")
