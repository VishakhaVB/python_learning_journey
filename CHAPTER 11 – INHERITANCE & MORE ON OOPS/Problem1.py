# 1. Create a class (2-D vector) and use it to create another class representing a 3-D 
# vector.

class Vector2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

    def add(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)


class Vector3D(Vector2D):
    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y)
        self.z = z

    def __repr__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

    def add(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + getattr(other, 'z', 0))


# Demo
v2 = Vector2D(1, 2)
print(v2)

v3 = Vector3D(3, 4, 5)
print(v3)

print(v3.add(Vector3D(1, 1, 1)))
