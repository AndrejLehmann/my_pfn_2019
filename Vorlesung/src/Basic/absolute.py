#!/usr/bin/env python3
x = -5
y = x
if y < 0:
  y = -y     # indent relative to if
print(y)
x = 100
if x < 0:
  y = -x   # indent relative to if
else:
  y = x    # indent relative to else
print(y)
