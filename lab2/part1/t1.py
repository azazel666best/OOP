class Rectangle:
    def __init__(self, length=1, width=1):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @length.setter
    def length(self, length):
        if not isinstance(length, float):
            raise TypeError
        if 0.0 > length > 20.0:
            raise ValueError
        self.__length = length


    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise TypeError
        if 0.0 > width > 20.0:
            raise ValueError
        self.__width = width

    def perimeter(self):
        return (self.__length + self.__width) * 2

    def area(self):
        return self.__length * self.__width


obj = Rectangle()
try:
    obj.width = 15.28
    obj.length = 2.85
    print('length:', obj.length, 'width:', obj.width)
    print('perimeter:', obj.perimeter())
    print('area:', obj.area())
except ValueError:
    print('ValueError')
except TypeError:
    print('TypeError')


