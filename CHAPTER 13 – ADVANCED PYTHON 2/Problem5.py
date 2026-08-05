# 5. Write a program to find the maximum of the numbers in a list using the reduce
# function.

from functools import reduce

nums = [3, 7, 2, 9, 4]
max_val = reduce(lambda a, b: a if a > b else b, nums)
print(max_val)
