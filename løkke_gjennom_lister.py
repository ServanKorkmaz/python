
def f(x, a, b):
    summen = 0
    for i in range(a, b):
        summen += x[i]
    return summen

# print(f([3, 1, 2, 0, 4], 1, 3)) 
# print(f([0, 5, 2], 0, 3))
# print(f([4, 1, 0, 9], 2, 6))
# print(f([2, 2, 2, 2, 2], 2, 2))
print(f([1, 0, 3, 1, 2], -1, 2))

