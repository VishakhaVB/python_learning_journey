# 7. Override the __len__() method on vector of problem 5 to display the dimension of the 
# vector.

class Vector:
    def __init__(self, components):
        self.components = list(components)

    def __len__(self):
        return len(self.components)

    def __repr__(self):
        return f"Vector({self.components})"


# Demo
v = Vector([1, 2, 3, 4])
print('Dimension:', len(v))
