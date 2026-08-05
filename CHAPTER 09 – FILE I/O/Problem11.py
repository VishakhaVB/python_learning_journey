# 11. Write a python program to rename a file to 'renamed_by_python.txt'.

import os


def rename_to_renamed_by_python(path):
	dirn = os.path.dirname(path) or '.'
	dst = os.path.join(dirn, 'renamed_by_python.txt')
	os.rename(path, dst)
	return dst


# Demo: create and rename
sample = 'to_rename.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('keep this content')

print(rename_to_renamed_by_python(sample))
