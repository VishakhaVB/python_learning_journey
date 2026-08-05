# 2. Write a program to print third, fifth and seventh element from a list using enumerate
# function.

def pick_elements(lst):
    indices = {3,5,7}
    result = []
    for i, val in enumerate(lst, start=1):
        if i in indices:
            result.append(val)
    return result


# Demo
sample = list(range(1, 11))
print('List:', sample)
print('3rd,5th,7th:', pick_elements(sample))
