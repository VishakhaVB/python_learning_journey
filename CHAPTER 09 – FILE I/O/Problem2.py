# 2. The game() function in a program lets a user play a game and returns the score
#    as an integer. You need to read a file 'Hi-score.txt' which is either blank or
#    contains the previous Hi-score. You need to write a program to update the Hi-
#    score whenever the game() function breaks the Hi-score.

import os


def game():
	# simple deterministic demo game returning a score
	return 42


def update_hi_score(score, path='Hi-score.txt'):
	try:
		if os.path.exists(path):
			with open(path, 'r', encoding='utf-8') as f:
				content = f.read().strip()
			hi = int(content) if content else 0
		else:
			hi = 0
	except ValueError:
		hi = 0

	if score > hi:
		with open(path, 'w', encoding='utf-8') as f:
			f.write(str(score))
		return True
	return False


# Demo
score = game()
print('New hi?' , update_hi_score(score))
