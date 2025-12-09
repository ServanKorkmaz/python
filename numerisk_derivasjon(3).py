import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = (x-2)**3
    return y

h = 0.01

x = np.linspace(0, 5, 51)

f_deriv = (f(x + h)) - f(x - h) / (2 * h)

plt.plot(x, f_deriv),
plt.show(),
