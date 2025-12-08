
from re import X


def loop(a, b, c):
    x = a
    while x <= c:
        x += b
    return x

# print(loop(0, 2, 5))
# print(loop(5, 0, 10))
# print(loop(2, -1, 5))
# print(loop(7, 3, 6))
# print(loop(1, 5, 20))

def calc(x, step, limit):
    while x != limit:
        x += step
    return x

# print(calc(0, 2, 10))
# print(calc(5, -2, -5))
# print(calc(3, 3, 5))
# print(calc(1, 0, 1))

def weird(a, b, c):
    x = a
    while x < c:
        x -= b
    return x

# print(weird(10, 5, 0))
# print(weird(1, 2, 5))
# print(weird(-1, 0, 3))
print(weird(0, -2, -6))



