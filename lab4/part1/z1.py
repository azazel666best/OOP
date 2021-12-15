from math import gcd


def reduction_dec(f):
    def reduction(self, other):
        obj = f(self, other)
        k = gcd(obj.numerator, obj.denominator)
        obj.numerator //= k
        obj.denominator //= k
        return obj

    return reduction


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError("numerator and denominator mast be int")
        if denominator == 0:
            raise ZeroDivisionError("denominator mast be !=0")
        k = gcd(numerator, denominator)
        self.numerator = numerator // k
        self.denominator = denominator // k

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator + other.numerator * self.denominator,
                            self.denominator * other.denominator)
        elif isinstance(other, int):
            return Rational(self.numerator + other * self.denominator,
                            self.denominator)
        else:
            return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator + other * self.denominator,
                            self.denominator)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator - other.numerator * self.denominator,
                            self.denominator * other.denominator)
        elif isinstance(other, int):
            return Rational(self.numerator - other * self.denominator,
                            self.denominator)
        else:
            return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int):
            return Rational(other * self.denominator - self.numerator,
                            self.denominator)
        else:
            return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.numerator,
                            self.denominator * other.denominator)
        elif isinstance(other, int):
            return Rational(self.numerator * other,
                            self.denominator)
        else:
            return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int):
            return Rational(self.numerator * other,
                            self.denominator)
        else:
            return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return Rational(self.numerator * other.denominator,
                            self.denominator * other.numerator)
        elif isinstance(other, int):
            return Rational(self.numerator,
                            self.denominator * other)
        else:
            return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int):
            return Rational(self.denominator * other,
                            self.numerator)
        else:
            return NotImplemented

    @reduction_dec
    def __iadd__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator + other.numerator * self.denominator
            self.denominator *= other.denominator
            return self
        elif isinstance(other, int):
            self.numerator += other * self.denominator
            return self
        else:
            return NotImplemented

    @reduction_dec
    def __isub__(self, other):
        if isinstance(other, Rational):
            self.numerator = self.numerator * other.denominator - other.numerator * self.denominator
            self.denominator *= other.denominator
            return self
        elif isinstance(other, int):
            self.numerator -= other * self.denominator
            return self
        else:
            return NotImplemented

    @reduction_dec
    def __imul__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.numerator
            self.denominator *= other.denominator
            return self
        elif isinstance(other, int):
            self.numerator *= other
            return self
        else:
            return NotImplemented

    @reduction_dec
    def __itruediv__(self, other):
        if isinstance(other, Rational):
            self.numerator *= other.denominator
            self.denominator *= other.numerator
            return self
        elif isinstance(other, int):
            self.denominator *= other
            return self
        else:
            return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Rational):
            return self.numerator == other.numerator and self.denominator == other.denominator
        elif isinstance(other, int):
            return self.numerator == other * self.denominator
        else:
            return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Rational):
            return self.numerator != other.numerator or self.denominator != other.denominator
        elif isinstance(other, int):
            return self.numerator != other * self.denominator
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator < other * self.denominator
        else:
            return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator <= other * self.denominator
        else:
            return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator > other * self.denominator
        else:
            return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rational):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        elif isinstance(other, int):
            return self.numerator >= other * self.denominator
        else:
            return NotImplemented

    def common(self):
        return f'{self.numerator}/{self.denominator}'

    def decimal(self):
        return self.numerator / self.denominator


try:
    a = Rational(4, 9)
    b = Rational(6, 5)
except TypeError as er:
    print('TypeError!', er)
except ValueError as er:
    print('ValueError!', er)
