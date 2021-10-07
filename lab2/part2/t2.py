class SPTF:
    def __init__(self, name='text'):
        self.__file = open(name).read()
        if not self.__file.isascii():
            raise Exception
        self.__characters = len(self.__file)
        self.__words = 0
        for word in self.__file.split():
            if not (word.isdigit() or (len(word) == 1 and not word.isalpha())):
                self.__words += 1
        self.__sentences = 0
        sentence_char = '!?.'
        for char in self.__file:
            if char in sentence_char:
                self.__sentences += 1

    @property
    def characters(self):
        return self.__characters

    @property
    def words(self):
        return self.__words

    @property
    def sentences(self):
        return self.__sentences


try:
    obj = SPTF()
    print(obj.sentences)
    print(obj.words)
    print(obj.characters)
except Exception:
    print('Error!')
