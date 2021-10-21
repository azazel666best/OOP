from math import gcd

# from numpy.char import isnumeric


class Rational:
    def __init__(self, numerator='1', denominator='1'):
        if not (numerator.isdigit() and denominator.isdigit()):
            raise TypeError
        numerator = int(numerator)
        denominator = int(denominator)
        if denominator == 0:
            raise ValueError
        k = gcd(numerator, denominator)
        self.__numerator = numerator // k
        self.__denominator = denominator // k

    def common(self):
        return f'{self.__numerator}/{self.__denominator}'

    def decimal(self):
        return self.__numerator / self.__denominator


try:
    a = Rational(input("Enter numerator: "), input("Enter denominator: "))
    print(a.common())
    print(a.decimal())
except TypeError:
    print('TypeError!')
except ValueError:
    print('ValueError!')
