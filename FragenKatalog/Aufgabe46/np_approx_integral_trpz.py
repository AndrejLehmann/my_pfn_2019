#!/usr/bin/env python3

import numpy as np

# !!! 586--594
def np_approx_integral_trpz(f, p, q, n):
    x_array = np.linspace(p, q, n)
    fsum = np.sum(f(x_array))
    d = (q - p) / n
    return d * (0.5 * (f(p) + f(q)) + fsum)


def f(x):
    return x**2


a = 0
b = 2
print('integral x**2 from {} to {} = {}'.format(a, b, np_approx_integral_trpz(f, a, b, 10000)))


