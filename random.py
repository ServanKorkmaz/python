# temp konvertering
from math import sqrt
from pickletools import pybytes


def celsius_til_fahrenheit(c):
    return (9/5) * c + 32

#print(celsius_til_fahrenheit(0))
#print(celsius_til_fahrenheit(100))

# areal av sirkel
def sirkel_areal(r):
    return 3.14 * r**2

#print(sirkel_areal(2))
#print(sirkel_areal(5))

# gjennomsnitt av tre tall
def gjennomsnitt(a, b, c):
    return (a + b + c) / 3
print(gjennomsnitt(2,4,6))
print(gjennomsnitt(10,20,30))

def kvadrat(x):
    return x**2
print(kvadrat(5))

def multpiplisere(a, b):
    return a * b
print(multpiplisere(3,4))

def pythagoras(a, b):
    return (a**2 + b**2)**0.5
print(pythagoras(3,4))
