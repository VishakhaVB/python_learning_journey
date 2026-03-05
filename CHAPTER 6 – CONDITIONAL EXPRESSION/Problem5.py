# 5. Write a program which finds out whether a given name is present in a list or not.

names = ["Alice", "Bob", "Charlie", "David", "Emma", "Frank"]

name_to_find = input("Enter a name to search: ")

if name_to_find in names:
    print(f"'{name_to_find}' is present in the list.")
else:
    print(f"'{name_to_find}' is NOT present in the list.")

print(f"\nAvailable names: {names}")
