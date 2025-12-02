

def f(x):

    summen = 0
    for i in range(len(x)): 
        if x[i] % 2 == 0:   # sjekker om det er partall
            summen += x[i]
    return summen


# kall funksjonen
print(f([2,3,4,5]))
print(f([3,5]))
print(f([-2,0,-2]))
