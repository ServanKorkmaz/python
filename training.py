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