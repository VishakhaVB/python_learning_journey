# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from 
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’. 

class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Pets(Animals):
    def __init__(self, name):
        super().__init__(name)


class Dog(Pets):
    def bark(self):
        return f"{self.name} says: Woof!"


# Demo
pet = Dog('Rex')
print(pet.speak())
print(pet.bark())
