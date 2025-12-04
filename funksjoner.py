# tuppel/liste funksjoner
def f(x):
    summen = 0
    for i in range(len(x)):
        if x[i] % 2 == 0:
            summen += x[i]
    return summen

# geometriske rekker
def geometrisk_rekke(r, n):
    summen = 0
    for i in range(n + 1):
        summen += r**i
    return summen

# while loop
def f(start, endring, stopp):
    x = start
    while x > stopp:
        x += endring
    return x
# print(f(5, 2, 6))
print(f(6, 1, 4))



    
