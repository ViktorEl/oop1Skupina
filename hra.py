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
        if not isinstance(sila, int):
            raise ValueError('chyba sila musi byt cele cislo')
        if sila < 1 or sila > 10:
            raise ValueError('chyba sila musi byt v rozsahu od 1 do 10')
        self.__sila = sila

    def get_sila(self):
        return self.__sila

    def utok(self):
        utok_sila = random.randrange(1, self.sila+1)
        return f'Bojovnik zaútočil mečom silou {utok_sila}'

class Kuzelnik(Bojovnik):

    def __init__(self, meno, uroven, zivoty, sila, mana):
        super().__init__(meno, uroven, zivoty, sila)
        self.__mana = mana
    
    def set_mana(self, mana):
        if not isinstance(mana, int):
            raise ValueError('chyba mana musi byt cele cislo')
        if mana < 0 or mana > 20:
            raise ValueError('chyba mana musi byt v rozsahu od 0 do 20')
        self.__mana = mana
    
    def get_mana(self):
        return self.__mana
    
    def utok(self):
        sila_utoku = random.randint(1, self.sila)
        ubytok_many = sila_utoku * 2
        if ubytok_many > self.__mana:
            raise ValueError('Nemozete zoslat kuzlo pretoze nemate dostatok many doplnte si manu')
        return f'Kuzelnik zautocil silou {sila_utoku} a pouzil na to {ubytok_many} many'
    
    def dopln_manu(self):
        self.__mana = 50
        return 'Doplnil si si manu na maximum'
    
class Paladin(Kuzelnik):

    def __init__(self, meno, uroven, zivoty, sila, mana):
        super().__init__(meno, uroven, zivoty, sila, mana)

    def utok(self):
        utok = random.randint(1, self.__sila)
        kombinovany_utok = utok * 2
        ubytok_many = utok * 3
        if ubytok_many > self.__mana:
            return f'Nemas dostatok many na kuzlo pouzil si len utok mecom silou {utok}'
        if kombinovany_utok > 20:
            self.__zivoty -= 2
            self.__mana -= ubytok_many
            return f'Pouzil si neskutocne kombo so silou {kombinovany_utok} so stratou many {ubytok_many} ale prisiel si o dva zivoty'
        else:
            self.__mana -= ubytok_many
            return f'Pouzil si kombo so silou {kombinovany_utok} a stratil si pri tom manu {ubytok_many}'