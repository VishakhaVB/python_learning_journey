# 3. Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute?

class MyClass:
    a = 5  # class attribute


# Demo
print('Class attribute before:', MyClass.a)
obj = MyClass()
obj.a = 0  # setting attribute on instance
print('Instance attribute obj.a =', obj.a)
print('Class attribute after setting instance.a:', MyClass.a)

# Answer: setting obj.a creates/sets an instance attribute; it does NOT change MyClass.a
