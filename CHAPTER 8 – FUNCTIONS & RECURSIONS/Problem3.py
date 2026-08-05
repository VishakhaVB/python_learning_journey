def print_no_newline(*args, **kwargs):
	"""Print without trailing newline (uses `end=''`)."""
	print(*args, end="", **kwargs)


# simple demo
print_no_newline("Hello")
print(" World")
