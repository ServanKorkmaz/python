
def trapesintergrasjon(f, a, b, n):
    h = (b - a) / n
    s = f(a) + f(b)

    for i in range(0, n):
        x_i = a + h*i

    s = s + f(x_i)

    s = s * (h/2)
    return s

