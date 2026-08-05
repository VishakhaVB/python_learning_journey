# 4. A file contains a word "Donkey" multiple times. You need to write a program
#    which replace this word with ##### by updating the same file.

def censor_donkey(path):
	try:
		with open(path, 'r', encoding='utf-8') as f:
			text = f.read()
	except FileNotFoundError:
		return False
	new = text.replace('Donkey', '#####')
	with open(path, 'w', encoding='utf-8') as f:
		f.write(new)
	return True


# Demo: create sample file and censor
sample = 'donkey.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('Donkey\nAnother Donkey here.')

print(censor_donkey(sample))
