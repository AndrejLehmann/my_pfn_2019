def partialsums(a):
    for i,ai in enumerate(a):
        yield sum(a[:i+1])

for psum in partialsums([3,2,3,4,2,9]):
    print("{} ".format(psum),end='')
