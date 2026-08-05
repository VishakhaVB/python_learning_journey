# 10. Write a program to wipe out the content of a file using python.

def wipe_file(path):
	with open(path, 'w', encoding='utf-8'):
		pass
	return True


# Demo
sample = 'wipe_demo.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('to be wiped')

print(wipe_file(sample))
