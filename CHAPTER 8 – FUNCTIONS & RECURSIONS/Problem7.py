# 7. Write a python function to remove a given word from a list ad strip it at the same
#    time.

def remove_and_strip(words, target):
	"""Remove all occurrences of `target` from `words` after stripping each item.

	Returns a new list with stripped items where the stripped item != target.
	"""
	return [w.strip() for w in words if w.strip() != target]


# simple demo
sample = [" apple ", "banana", " apple", "cherry "]
target = "apple"
print(remove_and_strip(sample, target))
