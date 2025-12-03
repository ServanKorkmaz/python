import numpy as np
import matplotlib.pyplot as plt

from newtons_metode import f_deriv

# sentraldifferanse
def f(x):
    y = np.sin(2*x) + x**2
    return y

h = 0.001

x = np.linspace(-2, 2, 101)     # 101 tall fra -2 til 2

# fremoverdifferanse
def f(x):
    return np.e**(-x) * np.cos(3*x)
    


h = 0.21
x = np.linspace(0, 2, 220)

f_deriv = (f(x**2 + h) - f(x**2)) / h

plt.plot(x, f_deriv, label="f'(x) numerisk")        # tegner en graf/plot
plt.legend()
plt.grid(True)     # True = rutenett på, False = rutenett av
plt.show()


# bakoverdifferanse
def f(x):
    return np.log(x + 1)

h = 0.05
x = np.linspace(0, 4)

f_deriv = (f(x) - f(x -h)) / h

plt.plot(x, f_deriv, label="f'(x) numerisk")
plt.legend()
plt.grid(True)
plt.show()


# derivasjon av polynomer
def f(x):
    return x**5 - 4*x**3 + 2*x - 7

h = 0.001
x = np.linspace(-3, 3, 601)

def f_deriv(x):
    return 5*x**4 - 12*x**2 + 2

# Numerisk derivert (sentraldifferanse)
f_deriv_numerisk = (f(x + h) - f(x - h)) / (2*h)

# Plotting
plt.plot(x, f(x), label="f(x)")
plt.plot(x, f_deriv(x), label="f'(x) analytisk", linestyle="--")
plt.plot(x, f_deriv_numerisk, label="f'(x) numerisk")

plt.legend()
plt.grid(True)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Derivasjon av polynomer")
plt.show()






