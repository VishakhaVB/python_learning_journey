import re

# Email Validation
email = input("Enter Email: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

if re.match(email_pattern, email):
    print("Valid Email")
else:
    print("Invalid Email")


# Mobile Number Validation
mobile = input("Enter Mobile Number: ")

mobile_pattern = r'^[6-9]\d{9}$'

if re.match(mobile_pattern, mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")
