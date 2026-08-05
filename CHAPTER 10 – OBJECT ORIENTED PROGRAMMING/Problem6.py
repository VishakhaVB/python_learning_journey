# 6. Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects.

class Demo:
    def __init__(harry, x):  # 'harry' used instead of 'self'
        harry.x = x

    def show(slf):  # 'slf' used instead of 'self'
        return slf.x


# Demo
d = Demo(10)
print('Value via show():', d.show())

# Yes — the name 'self' is just a convention; any valid identifier works as the first parameter.
