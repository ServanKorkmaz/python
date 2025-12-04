
def f(x, a, b):
    summen = 0
    for i in range(a, b):
        summen += x[i]
    return summen

# print(f([0, 1, 1, 0, 2], 0, 2)) # printer 1 -> range er 0, 2 = 0, 1. Ikke 2, fordi range tar ikke med slutt verdien. b regnes ikke med
print(f([2,1,1,0,0], 1, 5))