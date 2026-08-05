# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum_n(n):
	"""Return the sum of first n natural numbers using recursion."""
	if n <= 0:
		return 0
	return n + sum_n(n - 1)


# simple demo
n = 5
print(sum_n(n))
