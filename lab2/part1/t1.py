class Rectangle:
    def __init__(self):
        self.__length = 1
        self.__width = 1

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if 0.0 < length < 20.0:
            self.__length = length
        else:
            raise ValueError

    @width.setter
    def width(self, width):
        if 0.0 < width < 20.0:
            self.__width = width
        else:
            raise ValueError

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def area(self):
        return self.__length * self.__width


obj = Rectangle()
try:
    obj.length = float(input())
    obj.width = float(input())
    print('length:', obj.length, 'width:', obj.width)
    print('perimeter:', obj.perimeter())
    print('area:', obj.area())
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')
