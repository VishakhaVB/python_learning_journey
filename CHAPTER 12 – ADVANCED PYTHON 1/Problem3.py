# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.

# Demo using n=5 (replace with input for interactive use)
n = 5
table = [n * i for i in range(1, 11)]
print(f'Multiplication table for {n}:', table)
