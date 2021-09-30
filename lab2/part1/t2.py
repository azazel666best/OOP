from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
        k = gcd(numerator, denominator)
        self.__numerator = numerator // k
        self.__denominator = denominator // k

    def common(self):
        return str(self.__numerator) + '/' + str(self.__denominator)

    def decimal(self):
        return self.__numerator / self.__denominator


try:
    a = Rational(int(input()), int(input()))
    print(a.common())
    print(a.decimal())
except Exception:
    print('TypeError')
