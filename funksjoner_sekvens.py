
def f(x):
    summen = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            summen += x[i]
    return summen

print(f([2, 3, 4, 5]))

