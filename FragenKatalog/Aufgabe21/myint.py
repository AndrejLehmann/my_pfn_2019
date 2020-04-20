def myint(string):
    int_ = 0
    for n,c in enumerate(string):
        int_ += 10**(len(string)-1-n) * (ord(c)-ord('0'))
    return int_

print(myint('2'))
print(myint('12'))
print(myint('4021'))
