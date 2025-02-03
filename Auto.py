class Auta():

    def __init__(self, znacka, spotreba):
        self.__set_znacka(znacka)
        self.__set_spotreba(spotreba)

    def __set_znacka(self, znacka):
        if len(znacka) < 2:
            raise ValueError('chyba kratky nazov')
        else:
            self.__znacka = znacka

    def __set_spotreba(self, spotreba):
        if spotreba < 0:
            raise ValueError('chyba spotreba nemoze byt zaporna')
        else:
            self.__spotreba = spotreba

    def __get_znacka(self):
        return self.__set_znacka


    def __get_spotreba(self):
        return self.__set_spotreba

    znacka = property(__get_znacka)
    spotreba = property(__get_spotreba, __set_spotreba)

auto = ('BMW', 12.6)
print(auto)