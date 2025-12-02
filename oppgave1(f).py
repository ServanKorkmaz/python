
# a)
def s(t):
    return t**3 - 6*t**2 + 9*t + 1
print(s(0))
print(s(1))
print(s(2))

# b)

def gjennomsnittsfart(t0,t1):
    return (s(t1) - s(t0)) / (t1 - t0)

print(gjennomsnittsfart(0,2))

# c)
def fart_til_tiden(t0,t1):
    return (s(t1) - s(t0) / (t1 - t0))
print(fart_til_tiden(0,1))
print(fart_til_tiden(1,2))


