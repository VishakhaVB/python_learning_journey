# 2. Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user.

subject1 = float(input("Enter marks in subject 1 (out of 100): "))
subject2 = float(input("Enter marks in subject 2 (out of 100): "))
subject3 = float(input("Enter marks in subject 3 (out of 100): "))

total_marks = subject1 + subject2 + subject3
percentage = (total_marks / 300) * 100

if percentage >= 40 and subject1 >= 33 and subject2 >= 33 and subject3 >= 33:
    print(f"Congratulations! You have passed with {percentage:.2f}%")
else:
    print(f"Sorry! You have failed.")
    if percentage < 40:
        print(f"Total percentage {percentage:.2f}% is less than 40%")
    if subject1 < 33:
        print(f"Subject 1 marks ({subject1}) is less than 33%")
    if subject2 < 33:
        print(f"Subject 2 marks ({subject2}) is less than 33%")
    if subject3 < 33:
        print(f"Subject 3 marks ({subject3}) is less than 33%")
