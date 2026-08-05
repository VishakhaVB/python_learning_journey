# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded 
# operators ‘+’ and ‘*’ which adds and multiplies them. 

class Complex:
    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        # (a+bi)*(c+di) = (ac - bd) + (ad+bc)i
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __repr__(self):
        return f"({self.real} + {self.imag}i)"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print('Add:', c1 + c2)
print('Mul:', c1 * c2)
