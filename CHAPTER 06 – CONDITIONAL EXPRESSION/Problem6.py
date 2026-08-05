# 6. Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks = float(input("Enter your marks (0-100): "))

if marks > 100 or marks < 0:
    print("Invalid marks! Please enter marks between 0 and 100.")
elif marks >= 90:
    grade = "Ex"
elif marks >= 80:
    grade = "A"
elif marks >= 70:
    grade = "B"
elif marks >= 60:
    grade = "C"
elif marks >= 50:
    grade = "D"
else:
    grade = "F"

if 0 <= marks <= 100:
    print(f"Your grade is: {grade}")
