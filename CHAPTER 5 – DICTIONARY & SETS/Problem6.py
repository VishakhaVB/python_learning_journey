# Question 6:
# Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

dictionary = {}
name=input("Enter name of friend 1 : ")
language=input("Enter favorite language of friend 1 : ")
dictionary.update({name:language})

name=input("Enter name of friend 2 : ")
language=input("Enter favorite language of friend 2 : ")
dictionary.update({name:language})

name=input("Enter name of friend 3 : ")
language=input("Enter favorite language of friend 3 : ")
dictionary.update({name:language})

name=input("Enter name of friend 4 : ")
language=input("Enter favorite language of friend 4 : ")
dictionary.update({name:language})

print(dictionary)