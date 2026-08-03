import os

file_name = input("Enter file name: ")

if os.path.exists(file_name):
    print("File exists.")
else:
    print("File does not exist.")


