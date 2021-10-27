from re import match


class Product:
    def __init__(self, price, description, dimensions):
        self.price = round(price, 2)
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self.__price

    @property
    def description(self):
        return self.__description

    @property
    def dimensions(self):
        return self.__dimensions

    @price.setter
    def price(self, price):
        if not isinstance(price, (int, float)):
            raise TypeError
        if price <= 0:
            raise ValueError
        self.__price = price

    @description.setter
    def description(self, description):
        if not isinstance(description, str):
            raise TypeError
        self.__description = description

    @dimensions.setter
    def dimensions(self, dimensions):
        self.__dimensions = dimensions

    def __str__(self):
        return f'Prise: {self.__price}, description: {self.__description}, dimensions: {self.__dimensions};'


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone

    @property
    def surname(self):
        return self.__surname

    @property
    def name(self):
        return self.__name

    @property
    def patronymic(self):
        return self.__patronymic

    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @surname.setter
    def surname(self, surname):
        if not isinstance(surname, str):
            raise TypeError
        self.__surname = surname

    @name.setter
    def name(self, name):
        if not isinstance(name, str):
            raise TypeError
        self.__name = name

    @patronymic.setter
    def patronymic(self, patronymic):
        if not isinstance(patronymic, str):
            raise TypeError
        self.__patronymic = patronymic

    @mobile_phone.setter
    def mobile_phone(self, mobile_phone):
        if not isinstance(mobile_phone, str):
            raise TypeError
        if not match(r'\+380[0-9]{9}$', mobile_phone):
            raise ValueError
        self.__mobile_phone = mobile_phone

    def __str__(self):
        return f'Surname: {self.__surname}, name: {self.__name}, patronymic: {self.__patronymic}' \
               f', mobile phone: {self.__mobile_phone};'


class Order:
    def __init__(self, customer, *products):
        self.customer = customer
        self.products = list(products)

    @property
    def customer(self):
        return self.__customer

    @property
    def products(self):
        return self.__products

    @customer.setter
    def customer(self, customer):
        if not isinstance(customer, Customer):
            raise TypeError
        self.__customer = customer

    @products.setter
    def products(self, products):
        if not all(isinstance(x, Product) for x in products):
            raise TypeError
        self.__products = products

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product):
        self.__products.remove(product)

    def total_value(self):
        tv = 0
        for prod in self.__products:
            tv += prod.price
        return tv

    def __str__(self):
        return f'Customer: \n\t{self.__customer.__str__()}\nProducts:\n\t'+'\n\t'.join(map(str, self.__products))


try:
    customer = Customer('a', 's', 'd', '+380999999999')
    product1 = Product(1.255, 'w', 'e')
    product2 = Product(28.5, '1', 'e')

    order = Order(customer, product1, Product(2, 'x', 'c'))

    order.add_product(product2)
    order.remove_product(product1)

    print(order)
    print('Total value:', order.total_value())
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')
