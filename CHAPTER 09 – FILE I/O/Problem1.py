# 1. Write a program to read the text from a given file 'poems.txt' and find out
#    whether it contains the word 'twinkle'.

def contains_twinkle(path):
	"""Return True if file contains word 'twinkle' (case-insensitive)."""
	try:
		with open(path, 'r', encoding='utf-8') as f:
			text = f.read().lower()
		return 'twinkle' in text
	except FileNotFoundError:
		return False


# Demo: create a sample poems.txt and check
sample = 'poems.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('Twinkle twinkle little star\nHow I wonder what you are')

print(contains_twinkle(sample))
