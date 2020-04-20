class MyFloat():
    def __init__(self, f):
        self.val = f

    def __eq__(self, other):                 #|
        if abs(self.val - other.val) < 0.01: #|
            return True                      #| !!!
        else:                                #|
            return False                     #|


#>>> 3.145 - 3.13511
#0.009889999999999954
#>>> 3.14512 - 3.13511
#0.010009999999999852
flist = [3.145, 3.13511, 3.14512]
for i in range(len(flist)-1):
    fi = flist[i]
    for j in range(i+1,len(flist)):
        fj = flist[j]
        #print('{} {}'.format(MyFloat(fi), MyFloat(fj)))
        print('{:.2f} == {:.2f} => {}'.format(fi, fj, MyFloat(fi) == MyFloat(fj)))
