
# a)
def s(t):
    return t**3 - 6*t**2 + 9*t + 1      # returnerer funksjonen
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

# d)
def h(t):
    return -2*t**2 + 8*t + 3
print(h(0))
print(h(2))


# e)
def gjennomsnittshastighet(t0,t1):
    return (h(t1) - h(t0)) / (t1 - t0)

print(gjennomsnittshastighet(0,2))      # (0,2) = t0 and t1
print(gjennomsnittshastighet(2,3))

# f) Temperatur konvertering
celsius_til_fahrenheit(c) 
return (9/5) * c + 32




