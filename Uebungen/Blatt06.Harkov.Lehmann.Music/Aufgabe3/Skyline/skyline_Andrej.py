#!usr/bin/env python3
# Harkov.Lehmann.Music
# Bearbeitungszeit: 0.5h


# len(s(i)) = 2**i-1 with i=1,2,3,...(=IN\{0}=IN*)

def s(i):
    if i == 0:
        return ''
    else:
        return s(i-1)+chr(96+i)+s(i-1)


for i in range(1,10):
    print(s(i))
