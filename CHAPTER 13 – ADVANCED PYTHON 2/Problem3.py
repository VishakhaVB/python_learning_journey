# 3. A list contains the multiplication table of 7. write a program to convert it to vertical
# string of same numbers.

table7 = [7 * i for i in range(1, 11)]
vertical = '\n'.join(str(x) for x in table7)
print(vertical)
