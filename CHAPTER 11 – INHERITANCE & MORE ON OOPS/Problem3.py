# 3. Create a class ‘Employee’ and add salary and increment properties to it. 
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter 
# which changes the value of increment based on the salary. 

class Employee:
    def __init__(self, name, salary, increment=0.0):
        self.name = name
        self.salary = salary
        self.increment = increment

    @property
    def salaryAfterIncrement(self):
        return self.salary * (1 + self.increment)

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self, _):
        # adjust increment based on current salary
        if self.salary < 30000:
            self.increment = 0.10
        elif self.salary < 70000:
            self.increment = 0.05
        else:
            self.increment = 0.02


# Demo
emp = Employee('Alice', 25000)
print('Before:', emp.salary, 'increment=', emp.increment)
emp.salaryAfterIncrement = True  # triggers increment adjustment
print('After increment rate:', emp.increment)
print('Salary after increment:', emp.salaryAfterIncrement)
