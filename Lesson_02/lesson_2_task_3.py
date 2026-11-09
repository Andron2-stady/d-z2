import math

def square(side):
    if not isinstance(side, int):
        side = math.ceil(side)
    return side * side

print(square(5))
print(square(5.3))