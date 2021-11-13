class Date:
    months = ("січеня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня",
              "листопада", "грудня")

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @property
    def month(self):
        return self.__month

    @property
    def year(self):
        return self.__year

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError
        if 1 > day or day > 31:
            raise ValueError
        self.__day = day

    @month.setter
    def month(self, month):
        if not isinstance(month, int):
            raise TypeError
        if 1 > month or month > 12:
            raise ValueError
        self.__month = month

    @year.setter
    def year(self, year):
        if not isinstance(year, int):
            raise TypeError
        self.__year = year

    def str_1(self):
        months = ("січеня", "лютого", "березня", "квітня", "травня", "червня", "липня", "серпня", "вересня", "жовтня",
                  "листопада", "грудня")
        return f'{self.__day} {months[self.__month-1]} {self.__year} року'

    def str_2(self):
        return f'{self.__day:02}.{self.__month:02}.{self.__year}'


try:
    obj = Date(12, 2, 2020)
    print(obj.str_1())
    print(obj.str_2())
except TypeError as er:
    print("Error", er)
except ValueError as er:
    print("Error", er)
