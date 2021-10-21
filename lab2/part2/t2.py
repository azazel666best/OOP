from os.path import isfile
from re import findall


class SPTF:
    def __init__(self, name):
        if not isfile(name):
            raise Exception
        with open(name) as f:
            if not f.read().isascii():
                raise Exception
        self.__name = name

    def characters(self):
        with open(self.__name) as f:
            return len(f.read())

    def words(self):
        with open(self.__name) as f:
            # return len(findall(r'([A-z]+[A-z\'-][A-z]+)|[Az]+', f.read()))
            return len(findall(r'\b[-\w\']+\b', f.read()))

    def sentences(self):
        with open(self.__name) as f:
            return len(findall(r'[^!?.][\.!?]', f.read()))


try:
    obj = SPTF('text')
    print(obj.characters())
    print(obj.words())
    print(obj.sentences())
except Exception:
    print('Error!')
