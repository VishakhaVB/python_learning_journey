import os

# Specify the directory path
directory_path = "/"

# List all files and folders in the directory
contents = os.listdir(directory_path)

# Print the results
print(f"Contents of '{directory_path}':")
for item in contents:
    print(item)
