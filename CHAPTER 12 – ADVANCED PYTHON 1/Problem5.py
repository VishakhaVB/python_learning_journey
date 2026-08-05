# 5. Store the multiplication tables generated in problem 3 in a file named Tables.txt.

def write_table_to_file(n, filename='Tables.txt'):
    with open(filename, 'w', encoding='utf-8') as f:
        for i in range(1, 11):
            f.write(f'{n} x {i} = {n*i}\n')
    return filename


# Demo: write table for 5
print('Wrote:', write_table_to_file(5))
