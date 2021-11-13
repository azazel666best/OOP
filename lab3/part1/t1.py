from datetime import datetime


class Event:
    def __init__(self, name, num_of_tickets, base_price, date):
        self.name = name
        self.num_of_tickets = num_of_tickets
        self.base_price = base_price
        self.date = date
        self.tickets_id = []

    @property
    def name(self):
        return self.__name

    @property
    def num_of_tickets(self):
        return self.__num_of_tickets

    @property
    def base_price(self):
        return self.__base_price

    @property
    def date(self):
        return self.__date

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name mast be str')
        self.__name = name

    @num_of_tickets.setter
    def num_of_tickets(self, num_of_tickets):
        if not isinstance(num_of_tickets, int):
            raise TypeError('num of tickets mast be int')
        if num_of_tickets < 0:
            raise ValueError('num of tickets mast be >0')
        self.__num_of_tickets = num_of_tickets

    @base_price.setter
    def base_price(self, base_price):
        if not isinstance(base_price, (float, int)):
            raise TypeError('base prise mast be float or int')
        if base_price < 0:
            raise ValueError('base prise mast be >0')
        self.__base_price = base_price

    @date.setter
    def date(self, date):
        if not isinstance(date, datetime):
            raise TypeError('date mast be datetime')
        if date < datetime.now():
            raise ValueError('date mast be after now')
        self.__date = date

    def __str__(self):
        return f'{self.__name}, {self.__num_of_tickets}, {self.__base_price}, {self.__date}'


class Ticket:
    def __init__(self, event, ticket_id, date, is_student=False):
        self.event = event
        self.ticket_id = ticket_id
        self.is_student = is_student
        self.date = date

    @property
    def event(self):
        return self.__event

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def is_student(self):
        return self.__is_student

    @property
    def date(self):
        return self.__date

    @event.setter
    def event(self, event):
        if not isinstance(event, Event):
            raise TypeError('event mast be Event')
        self.__event = event

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        if not self.event.num_of_tickets:
            raise ValueError('No tickets')
        if not isinstance(ticket_id, int):
            raise TypeError('ticket id mast be int')
        if ticket_id in self.__event.tickets_id:
            raise ValueError('ticket id mast be unique')
        self.__ticket_id = ticket_id
        self.__event.num_of_tickets -= 1
        self.__event.tickets_id.append(ticket_id)

    @is_student.setter
    def is_student(self, is_student):
        if not isinstance(is_student, bool):
            raise TypeError('is student mast be bool')
        self.__is_student = is_student

    @date.setter
    def date(self, date):
        if not isinstance(date, datetime):
            raise TypeError('date mast be datatime')
        self.__date = date

    def get_price(self):
        if self.is_student:
            return round(self.event.base_price * 0.5, 2)
        elif (self.event.date - self.date).days >= 60:
            return round(self.event.base_price * 0.6, 2)
        elif (self.event.date - self.date).days < 10:
            return round(self.event.base_price * 1.1, 2)
        else:
            return round(self.event.base_price, 2)

    def __str__(self):
        return f'{self.ticket_id, self.is_student}'


try:
    obj = Event('asd', 2, 12.5, datetime(2025, 7, 14, 12, 30))
    ticket_1 = Ticket(obj, 152551, datetime(2025, 7, 12, 12, 30), False)
    ticket_2 = Ticket(obj, 152552, datetime(2025, 7, 12, 12, 30), False)
    print(obj.base_price)
    print(ticket_1.get_price())
except TypeError as er:
    print('TypeError', er)
except ValueError as er:
    print('ValueError', er)
