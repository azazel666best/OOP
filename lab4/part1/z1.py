from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError("numerator and denominator mast be int")
        if denominator == 0:
            raise ValueError("denominator mast be !=0")
        k = gcd(numerator, denominator)
        self.numerator = numerator // k
        self.denominator = denominator // k

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator + other * self.denominator,
                            self.denominator)
        else:
            raise TypeError

    def __radd__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator + other * self.denominator,
                            self.denominator)
        else:
            raise TypeError

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator - other * self.denominator,
                            self.denominator)
        else:
            raise TypeError

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(other * self.denominator - self.numerator,
                            self.denominator)
        else:
            raise TypeError

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator * other,
                            self.denominator)
        else:
            raise TypeError

    def __rmul__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator * other,
                            self.denominator)
        else:
            raise TypeError

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator,
                            self.denominator * other.numerator)
        if isinstance(other, int):
            return Rational(self.numerator,
                            self.denominator * other)
        else:
            raise TypeError

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(self.denominator * other,
                            self.numerator)
        else:
            raise TypeError

    def __iadd__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator + other * self.denominator,
                            self.denominator)
        else:
            raise TypeError

    def __isub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator - other * self.denominator,
                            self.denominator)
        else:
            raise TypeError

    def __imul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator,
                            self.denominator * other.denominator)
        if isinstance(other, int):
            return Rational(self.numerator * other,
                            self.denominator)
        else:
            raise TypeError

    def __itruediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator,
                            self.denominator * other.numerator)
        if isinstance(other, int):
            return Rational(self.numerator,
                            self.denominator * other)
        else:
            raise TypeError

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        if isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            raise TypeError

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.numerator != other.numerator or self.denominator != other.denominator
        if isinstance(other, int):
            return self.numerator != other * self.denominator
        else:
            raise TypeError

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            raise TypeError

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator <= other * self.denominator
        else:
            raise TypeError

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator > other * self.denominator
        else:
            raise TypeError

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        if isinstance(other, int):
            return self.numerator >= other * self.denominator
        else:
            raise TypeError

    def common(self):
        return f'{self.numerator}/{self.denominator}'

    def decimal(self):
        return self.numerator / self.denominator


try:
    a = Rational(4, 8)
    b = Rational(6, 14)
except TypeError as er:
    print('TypeError!', er)
except ValueError as er:
    print('ValueError!', er)
