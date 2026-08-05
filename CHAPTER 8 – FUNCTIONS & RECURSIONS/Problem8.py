def multiplication_table(n, upto=10):
	"""Print multiplication table for `n` up to `upto` (inclusive)."""
	for i in range(1, upto + 1):
		print(f"{n} x {i} = {n * i}")


# simple demo: print multiplication table for 5
n = 5
multiplication_table(n)
