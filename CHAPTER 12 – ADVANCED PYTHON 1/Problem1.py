# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

def open_three_files(paths):
    files = {}
    for p in paths:
        try:
            f = open(p, 'r', encoding='utf-8')
            files[p] = f
        except FileNotFoundError:
            print(f"File not found: {p}")
    return files


# Demo: attempt to open 1.txt, 2.txt, 3.txt (creates 2.txt for demo)
with open('2.txt', 'w', encoding='utf-8') as f:
    f.write('sample')

opened = open_three_files(['1.txt', '2.txt', '3.txt'])
for p, fh in opened.items():
    print(p, 'opened, size=', len(fh.read()))
    fh.close()
