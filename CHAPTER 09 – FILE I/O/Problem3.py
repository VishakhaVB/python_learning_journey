# 3. Write a program to generate multiplication tables from 2 to 20 and write it to the
#    different files. Place these files in a folder for a 13-year old.

import os

def gen_tables(folder='tables_for_13'):
	os.makedirs(folder, exist_ok=True)
	for n in range(2, 21):
		path = os.path.join(folder, f'table_{n}.txt')
		with open(path, 'w', encoding='utf-8') as f:
			for i in range(1, 11):
				f.write(f'{n} x {i} = {n*i}\n')

# Demo
gen_tables()
print('Tables written to tables_for_13/')
