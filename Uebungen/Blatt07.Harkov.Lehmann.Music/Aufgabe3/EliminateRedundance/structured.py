#!/usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 1h
import math

x_vector = [6,7,12,14,23,41,53,60,69,72,100,90]
y_vector = [2.5,1.1,6.3,2.1,2.9,15.3,20.7,18.4,22,33,50,43]
z_vector = [1,12,18,33,78,99,65,77,81,54,78,77]


def compare(a_vector,b_vector):
    assert len(a_vector) == len(b_vector) and len(a_vector) > 0
    a_m = math.fsum(a_vector)/len(a_vector)
    b_m = math.fsum(b_vector)/len(b_vector)
    a_b_diff_prod_sum = a_diff_sqr_sum = b_diff_sqr_sum = 0
    for i in range(len(a_vector)):
        a_diff = a_vector[i] - a_m
        b_diff = b_vector[i] - b_m
        a_b_diff_prod_sum += a_diff * b_diff
        a_diff_sqr_sum += a_diff * a_diff
        b_diff_sqr_sum += b_diff * b_diff
    return a_b_diff_prod_sum / math.sqrt(a_diff_sqr_sum * b_diff_sqr_sum)

print('x_vector/y_vector: {:.5f}'.format(compare(x_vector,y_vector)))
print('x_vector/z_vector: {:.5f}'.format(compare(x_vector,z_vector)))
print('y_vector/z_vector: {:.5f}'.format(compare(y_vector,z_vector)))
