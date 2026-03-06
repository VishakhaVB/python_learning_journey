# Question 8:
# If languages of two friends are same; what will happen to the program in problem 6?

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

# Enter name of friend 1 : pooja
# Enter favorite language of friend 1 : c++
# Enter name of friend 2 : sayali
# Enter favorite language of friend 2 : java
# Enter name of friend 3 : bhakti
# Enter favorite language of friend 3 : go
# Enter name of friend 4 : wish
# Enter favorite language of friend 4 : c++
# {'pooja': 'c++', 'sayali': 'java', 'bhakti': 'go', 'wish': 'c++'}