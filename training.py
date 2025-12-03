import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = np.sin(2*x) + x**2
    return y

h = 0.001

x = np.linspace(-2, 2, 101)     # 101 tall fra -2 til 2

print(np.linspace)
