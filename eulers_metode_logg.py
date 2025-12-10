import numpy as np
import matplotlib.pyplot as plt

h = 1
N = 100

x_n = 0
y_n = 5

y_logg = [y_n]
x_logg = [x_n]

for n in range(N):
    y_n = y_n - h*0.1*y_n
    x_n = x_n + h
    x_logg.append(x_n)
    y_logg.append(y_n)

plt.plot(x_logg, y_logg)
plt.show()

