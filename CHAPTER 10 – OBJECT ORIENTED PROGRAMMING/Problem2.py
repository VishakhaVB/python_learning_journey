# 2. Write a class “Calculator” capable of finding square, cube and square root of a 
# number.

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


# Demo
print('square(3)=', Calculator.square(3))
print('cube(3)=', Calculator.cube(3))
print('sqrt(9)=', Calculator.sqrt(9))
