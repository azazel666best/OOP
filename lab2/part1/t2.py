from math import gcd


class Rational:
    def __init__(self, numerator=1, denominator=1):
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
    a = Rational(int(input()), int(input()))
    print(a.common())
    print(a.decimal())
except Exception:
    print('Error!')
