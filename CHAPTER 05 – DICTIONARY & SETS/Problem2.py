# Question 2:
# Write a program to input eight numbers from the user and display all the unique
# numbers (once).

numbers = set()
num=input("Enter number 1  : ")
numbers.add(int(num))
num=input("Enter number 2  : ")
numbers.add(int(num))
num=input("Enter number 3  : ")
numbers.add(int(num))
num=input("Enter number 4  : ")
numbers.add(int(num))
num=input("Enter number 5  : ")
numbers.add(int(num))
num=input("Enter number 6  : ")
numbers.add(int(num))
num=input("Enter number 7  : ")
numbers.add(int(num))
num=input("Enter number 8  : ")
numbers.add(int(num))
print("Unique numbers are : ",numbers)

