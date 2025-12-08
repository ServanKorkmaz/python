
def loop(a, b, c):
    x = a
    while x <= c:
        x += b
    return x

# print(loop(0, 2, 5))
# print(loop(5, 0, 10))
# print(loop(2, -1, 5))
# print(loop(7, 3, 6))
print(loop(1, 5, 20))
