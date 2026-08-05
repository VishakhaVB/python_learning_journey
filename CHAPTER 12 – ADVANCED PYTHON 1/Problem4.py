# 4. Write a program to display a/b where a and b are integers. If b=0, display infinite by
# handling the 'ZeroDivisionError'.

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return 'infinite'


# Demo
print('10/2 =', safe_divide(10, 2))
print('10/0 =', safe_divide(10, 0))
