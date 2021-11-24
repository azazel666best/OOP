from datetime import datetime
import json


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
        return f'Name: {self.__name}\nNum of tickets: {self.__num_of_tickets}\nBase price: {self.__base_price}\n' \
               f'Date: {self.__date}'


class Ticket:
    def __init__(self, event, ticket_id, price):
        self.event = event
        self.ticket_id = ticket_id
        self.price = price

    @property
    def event(self):
        return self.__event

    @property
    def ticket_id(self):
        return self.__ticket_id

    @property
    def price(self):
        return self.__price

    @event.setter
    def event(self, event):
        if not isinstance(event, Event):
            raise TypeError('event mast be Event')
        self.__event = event

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('price mast be int or float')
        self.__price = price

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

    def __str__(self):
        return f'{self.event}\nTicket Id: {self.ticket_id}\nTicket price: {self.price}'


class UsualTicket(Ticket):
    def __init__(self, event, ticket_id):
        super(UsualTicket, self).__init__(event, ticket_id, round(event.base_price, 2))


class AdvanceTicket(Ticket):
    def __init__(self, event, ticket_id):
        with open('type_of_tickets') as file:
            super(AdvanceTicket, self).__init__(event, ticket_id, round(event.base_price *
                                                                        json.load(file)['AdvanceTicket'], 2))


class StudentTicket(Ticket):
    def __init__(self, event, ticket_id):
        with open('type_of_tickets') as file:
            super(StudentTicket, self).__init__(event, ticket_id, round(event.base_price *
                                                                        json.load(file)['StudentTicket'], 2))


class LateTicket(Ticket):
    def __init__(self, event, ticket_id):
        with open('type_of_tickets') as file:
            super(LateTicket, self).__init__(event, ticket_id, round(event.base_price *
                                                                        json.load(file)['LateTicket'], 2))


def get_ticket(event, ticket_id, date, is_student=False):
    if is_student:
        return StudentTicket(event, ticket_id)
    elif (event.date - date).days >= 60:
        return AdvanceTicket(event, ticket_id)
    elif (event.date - date).days < 10:
        return LateTicket(event, ticket_id)
    else:
        return UsualTicket(event, ticket_id)


try:
    obj = Event('asd', 4, 12, datetime(2025, 7, 14, 12, 30))
    ticket_us = get_ticket(obj, 152551, datetime(2025, 6, 13, 12, 30))
    ticket_st = get_ticket(obj, 152552, datetime(2025, 7, 13, 12, 30), True)
    ticket_ad = get_ticket(obj, 152553, datetime(2025, 7, 13, 12, 30))
    ticket_lt = get_ticket(obj, 152554, datetime(2025, 5, 13, 12, 30))
    print(ticket_us, end='\n\n')
    print(ticket_st, end='\n\n')
    print(ticket_ad, end='\n\n')
    print(ticket_lt, end='\n\n')
except TypeError as er:
    print('TypeError', er)
except ValueError as er:
    print('ValueError', er)
