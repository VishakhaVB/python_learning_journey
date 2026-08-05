# 7. Write a program to find out the line number where python is present from ques 6.

def lines_with_python(path):
	lines = []
	try:
		with open(path, 'r', encoding='utf-8') as f:
			for i, line in enumerate(f, 1):
				if 'python' in line.lower():
					lines.append(i)
	except FileNotFoundError:
		return []
	return lines


# Demo
sample = 'log.txt'
with open(sample, 'w', encoding='utf-8') as f:
	f.write('first line\npython appears here\nanother python here\n')

print(lines_with_python(sample))
