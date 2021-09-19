# Dunder methods
# __init__ , __add__, __mul__, __sub__, __eq__, __len__

class Fraction:
    def __init__(self, nr, dr=1):
        self.nr = nr
        self.dr = dr
        if self.dr < 0:
            self.nr *= -1
            self.dr *= -1
        self._reduce()

    def show(self):
        print(f'{self.nr}/{self.dr}')

    def __str__(self):
        return (f'{self.nr}/{self.dr}')

    def __repr__(self):
        return f'Fraction ({self.nr}, {self.dr})'


    def __mul__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.nr, self.dr * other.dr)
        f._reduce()
        return f

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr + self.dr *
                     other.nr, other.dr * self.dr)
        f._reduce()
        return f
    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        f = Fraction(self.nr * other.dr - self.dr *
                     other.nr, other.dr * self.dr)
        f._reduce()
        return f
    @staticmethod
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s

    def _reduce(self):
        h = Fraction.hcf(self.nr, self.dr)
        if h == 0:
            return
        self.nr //= h

        self.dr //= h
    def __eq__(self, other):
    	return self.nr * other.dr == self.dr * other.nr
    def __lt__(self, other):
    	return self.nr * other.dr < self.dr * other.nr
    def __le__(self, other):
    	return self.nr * other.dr <= self.dr * other.nr

# f1 = Fraction(1, 2)
# f2 = Fraction(2, 3)
# f3 = f1.__add__(f2)
# f3.show()
# f4 = f1 + f2
# f4.show()

# f5 = f1 - f2
# f5.show()

# f6 = f1 * f2
# f6.show()

# print(f1 == f2)
# print(f1 <= f2)


# a == b: a.__equal__(b)
# a!= b: a.__ne__(b)
# a < b: a.__lt__(b)
# a > b: a.__gt__(b)
# a <= b: a.__le__(b)
# a >= b: a.__ge__(b)


f1 = Fraction(2, 3)
f2 = Fraction(1, 3)
f3 = Fraction(9, 5)
# L  = {f1, f2, f3}
f = Fraction(2, 3)
print(f)
f
