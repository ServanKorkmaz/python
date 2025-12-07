def f(x, a, b):
    s = 0
    for i in range(a, b):
        s += x[i]
    return s
print(f([7, 1, 1, 7], -4, 2))