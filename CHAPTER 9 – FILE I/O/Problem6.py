# 6. Write a program to mine a log file and find out whether it contains 'python'.

def contains_python(path):
	try:
		with open(path, 'r', encoding='utf-8') as f:
			for line in f:
				if 'python' in line.lower():
					return True
	except FileNotFoundError:
		return False
	return False


# Demo
sample = 'log.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('Info: starting\nFound Python script\n')

print(contains_python(sample))
