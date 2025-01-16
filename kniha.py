
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

    def __get_nazov(self):
        return self.__nazov


    def __get_pocet(self):
        return self.__pocet_stran


    nazov = property(__get_nazov, __get_nazov) # atribut vytvorený cez property



kniha1 = Kniha('Zaklínač', 50)         # referencia na objekt/inštancia
kniha2 = Kniha('Harry Potter', 450)
kniha1.nazov = 'Poprežie'
kniha1.set_nazov = 'Zaklináč'



#print(kniha1.parametre_knihy())         # aplikovanie metody na objekt
#print(kniha1.pocet_stran)                # atribút
#print(kniha1.nazov)
#kniha1.pocet_stran = 380




        