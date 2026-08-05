# 9. Write a program to find out whether a file is identical and matches the content of
#    another file.

import filecmp


def files_identical(a, b):
	return filecmp.cmp(a, b, shallow=False)


# Demo: create two files and compare
a = 'a.txt'
b = 'b.txt'
with open(a, 'w', encoding='utf-8') as f:
	f.write('hello')
with open(b, 'w', encoding='utf-8') as f:
	f.write('hello')

print(files_identical(a, b))
