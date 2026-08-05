# Question 7:
# If the names of 2 friends are same; what will happen to the program in problem 6?



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

# Enter name of friend 1 : wish
# Enter favorite language of friend 1 : c++
# Enter name of friend 2 : pooja
# Enter favorite language of friend 2 : rust
# Enter name of friend 3 : sayali
# Enter favorite language of friend 3 : java
# Enter name of friend 4 : pooja
# Enter favorite language of friend 4 : python
# {'wish': 'c++', 'pooja': 'python', 'sayali': 'java'}