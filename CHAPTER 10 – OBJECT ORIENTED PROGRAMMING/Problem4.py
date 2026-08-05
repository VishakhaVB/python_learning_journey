# 4. Add a static method in problem 2, to greet the user with hello.

import math

class Calculator:
    @staticmethod
    def square(x):
        return x * x

    @staticmethod
    def cube(x):
        return x * x * x

    @staticmethod
    def sqrt(x):
        return math.sqrt(x)

    @staticmethod
    def greet():
        return 'Hello'

print(Calculator.greet())
print('square(4)=', Calculator.square(4))
