# Вычислить число c заданной точностью d

import math


def calc_pi(stop):
    pi = 0
    n = 1
    sg = 1
    while True:
        pi = pi + (4 / (2 * n - 1)) * sg
        if 4 / n < stop:
            return pi
        sg = -sg
        n += 1


acc = int(input("Введите точность в кол-во знаков после запятой: "))
print(math.pi)
print(round(calc_pi(10**-(acc+1)), acc))
