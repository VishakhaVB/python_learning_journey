# Problem 2: Write a program to accept marks of 6 students and display them in a sorted manner.

marks=[]
f1=int(input("Enter the marks of students 1 "))
marks.append(f1)
f2=int(input("Enter the marks of students 2 "))
marks.append(f2)
f3=int(input("Enter the marks of students 3 "))
marks.append(f3)
f4=int(input("Enter the marks of students 4 "))
marks.append(f4)
f5=int(input("Enter the marks of students 5 "))
marks.append(f5)
f6=int(input("Enter the marks of students 6 "))
marks.append(f6) 

marks.sort()
print("The list of marks is: ", marks)
