import pandas as pd

# Creating DataFrame
data = {
    'Employee': ['Amit', 'Riya', 'John', 'Sneha', 'Rahul'],
    'Department': ['IT', 'HR', 'Finance', 'IT', 'Marketing'],
    'Salary': [50000, 45000, 60000, 55000, 40000]
}

df = pd.DataFrame(data)

# Display DataFrame
print("Employee Data:\n")
print(df)

# Salary Analysis
print("\nSalary Analysis:\n")

print("Maximum Salary :", df['Salary'].max())
print("Minimum Salary :", df['Salary'].min())
print("Average Salary :", df['Salary'].mean())
print("Total Salary   :", df['Salary'].sum())

# Employees with salary greater than 50000
print("\nEmployees with Salary Greater than 50000:\n")
print(df[df['Salary'] > 50000])
