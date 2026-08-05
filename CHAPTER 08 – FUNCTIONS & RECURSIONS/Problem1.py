# 1. Write a program using functions to find greatest of three numbers.

def greatest_of_three(a, b, c):
	"""Return the greatest of three numbers."""
	return max(a, b, c)


# simple demo
a, b, c = 3, 7, 5
print(greatest_of_three(a, b, c))
