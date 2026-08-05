# 5. Repeat program 4 for a list of such words to be censored.

def censor_words(path, words):
	try:
		with open(path, 'r', encoding='utf-8') as f:
			text = f.read()
	except FileNotFoundError:
		return False
	for w in words:
		text = text.replace(w, '#' * len(w))
	with open(path, 'w', encoding='utf-8') as f:
		f.write(text)
	return True


# Demo
sample = 'censor_demo.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('Donkey is a word and badword is another.')

print(censor_words(sample, ['Donkey', 'badword']))
