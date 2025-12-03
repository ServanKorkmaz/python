
def f(x):
    y = x**4 + 2*x + 4
    return y

# funksjonens deriverte
def f_deriv(x):
    y = 4*x**3 + 2
    return y

# parametre
x_n = 0
tol = 1e-6

# newton's metode
while abs(f(x_n)) < tol:
    x_n -= f(x_n) / f_deriv(x_n)

# skriv ut resultatet
print(f"Løsning funnet i x = {x_n}")
