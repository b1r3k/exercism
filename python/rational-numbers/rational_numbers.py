from __future__ import division


def nwd(a, b):
    while b:
        c = a % b
        a = b
        b = c
    return a


class Rational(object):
    def __init__(self, numer, denom):
        self.numer = None
        self.denom = None
        self.set_values(numer, denom)

    def set_values(self, numer, denom):
        self.numer = numer
        if numer == 0:
            self.denom = 1
            return
        # move sign to numer
        sign = int(denom / abs(denom))
        self.denom = denom * sign
        self.numer *= sign
        self.reduce()
        return

    def reduce(self):
        n = nwd(abs(self.numer), abs(self.denom))
        self.numer = self.numer / n
        self.denom = self.denom / n

    def __eq__(self, other):
        try:
            return self.numer == other.numer and self.denom == other.denom
        except AttributeError:
            return False

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __sub__(self, other):
        numer = self.numer * other.denom - other.numer * self.denom
        denom = self.denom * other.denom
        return Rational(numer, denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        denom = self.denom * other.numer
        if denom == 0:
            raise ValueError('Denom equals 0')
        return Rational(self.numer * other.denom, denom)

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power == 0:
            return Rational(1, 1)
        if power > 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** power, self.numer ** power)

    def __rpow__(self, base):
        return (base ** self.numer) ** (1/self.denom)
