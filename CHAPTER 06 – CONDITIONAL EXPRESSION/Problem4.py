# 4. Write a program to find whether a given username contains less than 10 
# characters or not.

username = input("Enter your username: ")

if len(username) < 10:
    print(f"Username '{username}' contains less than 10 characters.")
else:
    print(f"Username '{username}' contains 10 or more characters.")
