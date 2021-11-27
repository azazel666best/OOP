from datetime import date
from re import match


class Person:
    def __init__(self, surname, name, phone, birthday):
        self.__birthday = birthday
        self.surname = surname
        self.name = name
        self.phone = phone
        self.birthday = birthday

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def phone(self):
        return self.__phone

    @property
    def birthday(self):
        return self.__birthday

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError('surname mast be str')
        self.__surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name mast be str')
        self.__name = name

    @phone.setter
    def phone(self, phone):
        if not isinstance(phone, str):
            raise TypeError('mobile_phone mast be str')
        if not match(r'\+380[\d]{9}$', phone):
            raise ValueError('mobile_phone mast be like +380762345657')
        self.__phone = phone

    @birthday.setter
    def birthday(self, birthday):
        if not isinstance(birthday, date):
            raise TypeError('birthday mast be date')
        if birthday > date.today():
            raise ValueError('birthday mast be not in tha future')
        self.__birthday = birthday

    def __str__(self):
        return f'Surname: {self.surname};\nName: {self.name};\nPhone: {self.phone}\nBirthday: {self.birthday}'


class Notebook:
    def __init__(self, *persons):
        self.persons = list(persons)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, persons):
        if not all(isinstance(person, Person) for person in persons):
            raise TypeError("all persons must be Person")
        self.__persons = persons

    def __str__(self):
        return '\n\n'.join(list(map(str, self.persons)))

    def __add__(self, person):
        if not isinstance(person, Person):
            raise TypeError('person mast be Person')
        self.persons.append(person)

    def __sub__(self, person):
        if not isinstance(person, Person):
            raise TypeError('person mast be Person')
        self.persons.remove(person)

    def __mul__(self, arg):
        res = []
        if not isinstance(arg, dict):
            raise TypeError('arg mast by dict')
        if not all(x in ('surname', 'name', 'phone', 'birthday') for x in list(arg.keys())):
            raise ValueError('Not such data field')

        for person in self.__persons:
            if all(arg[field] == self.f(person, field) for field in list(arg.keys())):
                res.append(person)

        return res

    @staticmethod
    def f(person, field):
        return eval('person.' + field)


p1 = Person('q', 'a', '+380000000000', date(2000, 1, 1))
p2 = Person('w', 's', '+380000000001', date(2000, 1, 2))
p3 = Person('q', 'd', '+380000000002', date(2000, 1, 3))

notebook = Notebook(p1, p2, p3, Person('r', 'f', '+380000000004', date(2000, 1, 4)))
for i in notebook * {'surname': 'q', 'birthday': date(2000, 1, 3)}:
    print(i, end='\n\n')
