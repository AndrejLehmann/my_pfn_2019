#!/usr/bin/env python3

def gcd(x, y):
    xi = x
    yi = y
    while (xi % yi) != 0:
        xi_1 = xi
        xi = yi
        yi = xi_1 % yi
    return yi

x = 18
y = 24
print('{} {} : gcd = {}'.format(x, y, gcd(x, y)))


