from re import match
import json


class Dish:
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError('name mast be str')
        self.__name = name

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError('price mast be int or float')
        if price <= 0:
            raise ValueError('price mast be >0')
        self.__price = price

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError('description mast be str')
        self.__description = description

    def __str__(self):
        return f'Name: {self.__name}, prise: {self.__price}, description: {self.__description};'


class Customer:
    def __init__(self, surname, name, mobile_phone):
        self.surname = surname
        self.name = name
        self.mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def mobile_phone(self):
        return self.__mobile_phone

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

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if not isinstance(mobile_phone, str):
            raise TypeError('mobile_phone mast be str')
        if not match(r'\+380[\d]{9}$', mobile_phone):
            raise ValueError('mobile_phone mast be like +380762345657')
        self.__mobile_phone = mobile_phone

    def __str__(self):
        return f'Surname: {self.__surname}, name: {self.__name}, mobile phone: {self.__mobile_phone};'


class Order:
    def __init__(self, new_customer, product, **ingredients):
        self.customer = new_customer
        self.product = product
        self.ingredients = ingredients

    @property
    def customer(self):
        return self.__customer

    @property
    def product(self):
        return self.__product

    @property
    def ingredients(self):
        return self.__ingredients

    @customer.setter
    def customer(self, new_customer):
        if not isinstance(new_customer, Customer):
            raise TypeError('customer mast be Customer')
        self.__customer = new_customer

    @product.setter
    def product(self, product):
        if not isinstance(product, Dish):
            raise TypeError('product mast be Pizza')
        self.__product = product

    @ingredients.setter
    def ingredients(self, ingredients):
        if not all(isinstance(x, str) for x in list(ingredients.keys())):
            raise TypeError('ingredients mast be Pizza')
        with open('ingredients', 'r') as file:
            ing_list = json.load(file)
            if not all(x in ing_list for x in list(ingredients.keys())):
                raise ValueError('no ingredient')

        self.__ingredients = ingredients

    def __str__(self):
        return f'Customer: \n\t{self.__customer}\nPizza:\n\t {self.__product}\nWith:\n\t' + \
               '\n\t'.join(list(map(lambda x: str(x) + ' ' + str(self.__ingredients[x]),
                                    list(self.__ingredients.keys()))))


class PizzaOfTheDay(Dish):
    def __init__(self, name, price, description, day):
        super(PizzaOfTheDay, self).__init__(name, price, description)
        self.day = day

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, day):
        if not isinstance(day, int):
            raise TypeError('day mast be int')
        if day < 0 or day > 6:
            raise TypeError('day mast be in range(7)')
        self.__day = day


class CustomEncoder(json.JSONEncoder):

    def default(self, o):
        if not isinstance(o, PizzaOfTheDay):
            raise TypeError
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def decode_object(o):
    if '__PizzaOfTheDay__' in o:
        return PizzaOfTheDay(o['__PizzaOfTheDay__']['_Dish__name'],
                             o['__PizzaOfTheDay__']['_Dish__price'],
                             o['__PizzaOfTheDay__']['_Dish__description'],
                             o['__PizzaOfTheDay__']['_PizzaOfTheDay__day'])
    return o


try:
    with open('pizza_of_the_day', 'r') as file:
        pizza_of_the_day = json.load(file, object_hook=decode_object)['tue']

    customer = Customer('a', 's', '+380999999999')

    order = Order(customer, pizza_of_the_day, a=1)

    print(order)
except TypeError as er:
    print(er)
except ValueError as er:
    print(er)
