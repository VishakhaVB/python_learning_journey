# Write a python program to print the contents of a directory using the os module.

# Search online for the function which does that.


import os

# Specify the directory path
directory_path = "/"

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print the results
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)
