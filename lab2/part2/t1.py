class Product:
    def __init__(self, price, description, dimensions):
        if (isinstance(price, float) or isinstance(price, int)) and isinstance(description, str):
            if price > 0:
                self.__price = round(price, 2)
            else:
                raise ValueError
            self.__description = description
        else:
            raise TypeError
        self.__dimensions = dimensions

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f'Prise: {self.__price}, description: {self.__description}, dimensions: {self.__dimensions};'


class Customer:
    def __init__(self, surname, name, patronymic, mobile_phone):
        if isinstance(mobile_phone, int) and isinstance(surname, str) and isinstance(name, str) \
                and isinstance(patronymic, str):
            self.__surname = surname
            self.__name = name
            self.__patronymic = patronymic
            self.__mobile_phone = mobile_phone
        else:
            raise TypeError

    def __str__(self):
        return f'Surname: {self.__surname}, name: {self.__name}, patronymic: {self.__patronymic}' \
               f', mobile phone: {self.__mobile_phone};'


class Order:
    def __init__(self, customer, *products):
        if isinstance(customer, Customer):
            self.__customer = customer
        else:
            raise Exception
        if all(isinstance(x, Product) for x in products):
            self.__products = products
        else:
            raise Exception

    def total_value(self):
        tv = 0
        for prod in self.__products:
            tv += prod.price
        return tv

    def __str__(self):
        return f'Customer: \n\t{self.__customer.__str__()}\nProducts:\n\t'+'\n\t'.join(map(str, self.__products))


try:
    customer = Customer('a', 's', 'd', 380661366613)
    product = Product(1.25555, 'w', 'e')
    order = Order(customer, product, Product(2, 'x', 'c'))

    print(order)
    print('Total value:', order.total_value())
except TypeError:
    print('TypeError')
except ValueError:
    print('ValueError')
