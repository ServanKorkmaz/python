
from re import I


def geometrisk_rekke(r, n):
    summen = 0
    for i in range(n + 1):
        summen += r**i

    return summen