from math import e
import numpy as np
import matplotlib.pyplot as plt

h = 0.05

def p(t):
    return 100 * (1 - e**(-0.3*t))

# lag t-verdier
t = np.linspace(0, 5, 101)

# numerisk derivasjon med sentral differanse
dpdt = p(t)(p, t, h, metode="senter")

# plott begge kurver
plt.plot(t, p(t), label="p(t)")
plt.plot(t, dpdt, label="p'(t) numerisk")
plt.legend()
plt.show()


