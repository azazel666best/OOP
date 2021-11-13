class Business_notebook:
    def __init__(self, **kvargs):
        self.__days = dict.fromkeys(("san", "mon", "tue", 'wed', "thu", 'fri', 'sat'), None)
        if not all(x in list(self.__days.keys()) for x in list(kvargs.keys())):
            raise NameError
        lst = []
        for x in self.__days:
            if kvargs.get(x):
                lst.append(kvargs.get(x))
        if not all(isinstance(x, str) for x in lst):
            raise TypeError

        for x in kvargs:
            self.__days[x] = kvargs[x]
        # self.__days = ("san", "mon", "tue", 'wed', "thu", 'fri', 'sat')

    def __str__(self):
        return list(self.__days.items()).__str__()

    def add_task(self, day, task):
        if not (day in self.__days):
            raise NameError
        if not isinstance(task, str):
            raise TypeError
        if self.__days[day]:
            self.__days[day] += '\n' + task
        else:
            self.__days[day] = task

    def correct_task(self, day, task1, task2):
        if not (day in self.__days):
            raise NameError
        if not (isinstance(task1, str) and isinstance(task2, str)):
            raise TypeError
        self.__days[day].replace(task1, task2)

    def dell_task(self, day, task):
        if not (day in self.__days):
            raise NameError
        if not isinstance(task, str):
            raise TypeError
        self.__days[day].replace(task, '')


try:
    a = 'asd'
    obj = Business_notebook(mon="asd")
    obj.add_task('mon', "qwe")
    obj.add_task('fri', "qwe")
    obj.correct_task('mon', 'asd', 'zxc')
    print(obj)
except NameError:
    print('Error!')
except TypeError:
    print('Error!2')
