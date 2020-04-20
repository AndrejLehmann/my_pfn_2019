def f(u,v):
    u += 't'
    v[3] = 't'

u = 'ccg'
v = ['c', 'c', 'g', 'g']
f(u,v)
print('u={}\nv={}'.format(u, ''.join(v)))
