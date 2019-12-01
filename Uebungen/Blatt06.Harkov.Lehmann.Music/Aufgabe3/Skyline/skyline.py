# !usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 1h

import sys

sys.setrecursionlimit(1500)

alphabet = ''
a = ord('a')

# produce the alphabet
for i in range(a,a+26):
   alphabet+= chr(i)
print(alphabet)

#define recursive function
def sky(j):
    if j == 0:
        return j
    return str(j-1)+str(j)+str(j-1)


# create the skyline string
for j in range(1,9):
    print('{}'.format((sky(j))))

