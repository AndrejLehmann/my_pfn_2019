#!usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 

alphabet = ''
a = ord('a')

# produce the alphabet
for i in range(a,a+26):
   alphabet+= chr(i)
print(alphabet)


def sky(j):
    if j == 0:
        return j
    return sky(j-1)+sky(j)+sky(j-1)


# create the skyline string with an recursive function
for j in range(1,9):
    print('{}'.format(sky(alphabet)))

