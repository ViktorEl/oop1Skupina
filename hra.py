import random

class Postava():

    def __init__(self, meno, uroven, zivoty):
        self.set_meno(meno)
        self.set_uroven(uroven)
        self.set_zivoty(zivoty)

    def utok(self):
        return 'Postava útočí'
    
    def get_meno(self):
        return self.__meno
    
    def get_uroven(self):
        return self.__uroven
    
    def get_zivoty(self):
        return self.__zivoty
    
    def set_meno(self, meno):
        if meno == '':
            raise ValueError('chyba musite zadat meno')
        self.__meno = meno
        
    def set_uroven(self, uroven):
        try:
            uroven = int(uroven)
        except ValueError:
            raise ValueError('Chyba uroven musi byt cele cislo')
        if uroven < 1 or uroven > 5:
            raise ValueError('chyba nespravna hodnota urovne')
        self.__uroven = uroven

    def set_zivoty(self, zivoty):
        try:
            zivoty = int(zivoty)
        except ValueError:
            raise ValueError('chyba zivoty musia byt cele cislo')
        if zivoty < 0 or zivoty > 20:
            raise ValueError('chyba nespravna hodnota zivotov')
    

class Bojovnik(Postava):

    def __init__(self, meno, uroven, zivoty, sila):
        super().__init__(meno, uroven, zivoty)
        self.set_sila(sila)

    def set_sila(self, sila):
        if isinstance(sila, int):
            raise ValueError('chyba sila musi byt cele cislo')
        if sila < 1 or sila > 10:
            raise ValueError('chyba sila musi byt v rozsahu od 1 do 10')
        self.__sila = sila

    def get_sila(self):
        return self.__sila

    def utok(self):
        utok_sila = random.randrange(1, self.sila+1)
        return f'Bojovnik zaútočil mečom silou {utok_sila}'
    