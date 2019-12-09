#!/usr/bin/env python3
import math
x_vector = [6,7,12,14,23,41,53,60,69,72,100,90]
y_vector = [2.5,1.1,6.3,2.1,2.9,15.3,20.7,18.4,22,33,50,43]
z_vector = [1,12,18,33,78,99,65,77,81,54,78,77]
assert len(x_vector) == len(y_vector) and len(x_vector) > 0
x_sum = 0
x_count = 0
for i in range(len(x_vector)):
  x_sum += x_vector[i]
  x_count += 1
y_sum = 0
y_count = 0
for j in range(len(y_vector)):
  y_sum += y_vector[j]
  y_count += 1
x_m = x_sum/x_count
y_m = y_sum/y_count
x_y_diff_prod_sum = 0
x_diff_sqr_sum = 0
y_diff_sqr_sum = 0
for i in range(len(x_vector)):
  x_diff = x_vector[i] - x_m
  y_diff = y_vector[i] - y_m
  x_y_diff_prod_sum += x_diff * y_diff
  x_diff_sqr_sum += x_diff * x_diff
  y_diff_sqr_sum += y_diff * y_diff
res_x_y = x_y_diff_prod_sum / math.sqrt(x_diff_sqr_sum * y_diff_sqr_sum)
print('x_vector/y_vector: {:.5f}'.format(res_x_y))
assert len(x_vector) == len(z_vector) and len(x_vector) > 0
x_sum = 0
x_count = 0
for i in range(len(x_vector)):
  x_sum += x_vector[i]
  x_count += 1
z_sum = 0
z_count = 0
for j in range(len(z_vector)):
  z_sum += z_vector[j]
  z_count += 1
x_m = x_sum/x_count
z_m = z_sum/z_count
x_z_diff_prod_sum = 0
x_diff_sqr_sum = 0
z_diff_sqr_sum = 0
for i in range(len(x_vector)):
  x_diff = x_vector[i] - x_m
  z_diff = z_vector[i] - z_m
  x_z_diff_prod_sum += x_diff * z_diff
  x_diff_sqr_sum += x_diff * x_diff
  z_diff_sqr_sum += z_diff * z_diff
res_x_z = x_z_diff_prod_sum / math.sqrt(x_diff_sqr_sum * z_diff_sqr_sum)
print('x_vector/z_vector: {:.5f}'.format(res_x_z))
assert len(y_vector) == len(z_vector) and len(y_vector) > 0
y_sum = 0
y_count = 0
for i in range(len(y_vector)):
  y_sum += y_vector[i]
  y_count += 1
z_sum = 0
z_count = 0
for j in range(len(z_vector)):
  z_sum += z_vector[j]
  z_count += 1
y_m = y_sum/y_count
z_m = z_sum/z_count
y_z_diff_prod_sum = 0
y_diff_sqr_sum = 0
z_diff_sqr_sum = 0
for i in range(len(y_vector)):
  y_diff = y_vector[i] - y_m
  z_diff = z_vector[i] - z_m
  y_z_diff_prod_sum += y_diff * z_diff
  y_diff_sqr_sum += y_diff * y_diff
  z_diff_sqr_sum += z_diff * z_diff
res_y_z = y_z_diff_prod_sum / math.sqrt(y_diff_sqr_sum * z_diff_sqr_sum)
print('y_vector/z_vector: {:.5f}'.format(res_y_z))
