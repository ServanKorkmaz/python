def f(x, a, b):
    s = 0
    for i in range(a, b):
        s += x[i]
    return s
print(f([2,2,2,2,], 1, -1))