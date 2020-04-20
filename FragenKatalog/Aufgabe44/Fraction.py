def gcd(x, y):
    xi = x
    yi = y
    while (xi % yi) != 0:
        xi_1 = xi
        xi = yi
        yi = xi_1 % yi
    return yi


class Fraction:
    def __init__(self, top, bottom):
        common = gcd(top, bottom)
        sel.num = top // common
        sel.den = bottom // common

    def __str__(self):
        if self.den == 1:
            return "{}".format(self.num)
        else:
            return "{}/{}".format(self.num, self.den)

    def __add__(self, oFrac):                         #|
        num = self.num*oFrac.den + oFrac.num*self.den #| !!!
        den = self.den*oFrac.den                      #|
        return Fraction(num, den)                     #|


