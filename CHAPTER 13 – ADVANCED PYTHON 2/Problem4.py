# 4. Write a program to filter a list of numbers which are divisible by 5.

nums = list(range(1, 51))
div5 = [x for x in nums if x % 5 == 0]
print(div5)
