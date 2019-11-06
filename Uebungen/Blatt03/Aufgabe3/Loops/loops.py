#!/usr/bin/env python3

n = 10
import sys

print("==== 1 =====")
# [1] convert to while loop:
i = 1
while i < n:
    print(i)
    i += 3
"""
for i in range(1, n, 3):
  print(i)
"""

# [2] convert to for loop:
print("==== 2 =====")
for i in range(0,int(n/2),1):
    j = n - i
    print(i,j)
"""
i = 0
j = n
while i < j:
  print(i, j)
  i += 1
  j -= 1
"""

# [3] convert to while loop:
print("==== 3 =====")
i = n
while i > -n : 
    print(i)
    i -= 1
"""
for i in range(n, -n, -1):
  print(i)
"""

# [4] convert to for loop:
print("==== 4 =====")
for i in range(1,n+1,1):
    print(i)
"""
i = 1
while True:
  print(i)
  i += 1
  if i > n:
    break
"""
