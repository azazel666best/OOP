import sys


class Rational:
    def __init__(self, numerator=1, denominator=1):
        if isinstance(numerator, int) and isinstance(denominator, int):
            self.__numerator = numerator
            self.__denominator = denominator
        else:
            raise TypeError

    def f(self):
        return self.__numerator + self.__denominator

try:
    a = Rational(3, 4)
    print(a.f())
except TypeError:
    print('TypeError')


