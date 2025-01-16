
class Kniha():

    def __init__(self, nazov, pocet_stran):         # inicializacna metoda/konštruktor
        self.__set_nazov(nazov)                         
        self.__set_pocet_stran(pocet_stran)

    def parametre_knihy(self):
        return f'Názov {self.__nazov}, počet strán {self.__pocet_stran}'

    def __set_nazov(self, nazov):
        knihy = ['Zaklínač', 'Harry Potter', 'Pobrežie', 'Hory', 'Tatry']
        if nazov not in knihy:
            raise ValueError('chyba')
        else:
            self.__nazov = nazov

    def __set_pocet_stran(self, pocet):
        if pocet < 5 or pocet > 1000:
            raise ValueError('chyba nesplnate pocet')
        else:
            self.__pocet_stran = pocet

    def get_meno(self):
        return self.__nazov


    def get_pocet(self):
        return self.__pocet_stran




kniha1 = Kniha('Zaklínač', 50)         # referencia na objekt/inštancia
kniha2 = Kniha('Harry Potter', 450)
print(kniha1.get_meno())

#print(kniha1.parametre_knihy())         # aplikovanie metody na objekt
#print(kniha1.pocet_stran)                # atribút
#print(kniha1.nazov)
#kniha1.pocet_stran = 380




        