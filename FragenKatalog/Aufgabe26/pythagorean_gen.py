def pythagorean_gen(n):
    from math import sqrt
    for j in range(n+1):
        for i in range(1, j+1):
            k2 = i**2 + j**2
            k = sqrt(k2)
            if k % 1 == 0: # !!!
                yield i, j, int(k)


n = 12
for i, j, k in pythagorean_gen(n):
    print(i,j,k)
