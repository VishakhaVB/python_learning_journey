# 8. Write a program to make a copy of a text file 'this.txt'.

import shutil


def copy_file(src, dst):
	try:
		shutil.copyfile(src, dst)
		return True
	except FileNotFoundError:
		return False


# Demo: create this.txt and copy it
src = 'this.txt'
dst = 'this_copy.txt'
with open(src, 'w', encoding='utf-8') as f:
	f.write('sample content')

print(copy_file(src, dst))
