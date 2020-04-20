def MyFloat(f):
    f = '{:>6.3f}'.format(f)
    return f


for f in [42.678, 3.1, 0.123456]:
    mf = MyFloat(f)
    print('"{}"'.format(mf))
