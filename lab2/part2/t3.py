class STUDENT:
    def __init__(self, name, surname, record_book_number, *grades):
        if not (isinstance(name, str) and isinstance(surname, str) and isinstance(record_book_number, int) and \
                all(isinstance(x, int) for x in grades)):
            raise TypeError
        self.__name = name
        self.__surname = surname
        self.__record_book_number = record_book_number
        self.__grades = grades

    def average_score(self):
        return sum(self.__grades) / len(self.__grades)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def record_book_number(self):
        return self.__record_book_number

    @property
    def grades(self):
        return self.__grades

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        self.__name = surname

    @record_book_number.setter
    def record_book_number(self, record_book_number):
        if not isinstance(record_book_number, int):
            raise TypeError
        self.__record_book_number = record_book_number

    @grades.setter
    def grades(self, grades):
        if not all(isinstance(x, int) for x in grades):
            raise TypeError
        self.__name = grades

    def __str__(self):
        return f'{self.__name}, {self.__surname}, {self.__record_book_number}, {self.average_score()}; ' \
               + ', '.join(map(str, self.__grades))


class GROUP:
    def __init__(self, *students):
        self.__count = 0
        if not all(isinstance(x, STUDENT) for x in students):
            raise TypeError
        self.__students = []
        for student in students:
            self.add_student(student)

    def add_student(self, new_student):
        if all((new_student.name, new_student.surname) != (student.name, student.surname) \
               for student in self.__students) and self.__count < 20:
            self.__students.append(new_student)
            self.__count += 1
        else:
            raise ValueError

    def dell_student(self, name, surname):
        if not (isinstance(name, str) and isinstance(surname, str)):
            raise TypeError
        for student in self.__students:
            if (student.name, student.surname) == (name, surname):
                self.__students.remove(student)
                self.__count -= 1

    def top5(self):
        students_list = list(self.__students)
        students_list.sort(key=lambda x: x.average_score(), reverse=True)
        return students_list[:5]

    def __str__(self):
        return '\n'.join(map(str, self.__students))


try:
    obj1 = STUDENT('q', 'a', 123, 12, 13, 14, 15)
    obj2 = STUDENT('w', 's', 123, 15, 13, 14, 15)
    obj3 = STUDENT('e', 'd', 123, 12, 14, 14, 15)
    obj4 = STUDENT('r', 'f', 123, 12, 13, 14, 15)
    obj5 = STUDENT('t', 'g', 123, 12, 13, 17, 15)
    obj6 = STUDENT('y', 'h', 123, 12, 12, 14, 15)
    group = GROUP(obj1, obj2, obj3, obj4, obj5, obj6, STUDENT('a', 's', 456, 5, 4, 3))
    group.dell_student('q', 'a')
    lst = group.top5()
    for i in range(5):
        print(lst[i])
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')
