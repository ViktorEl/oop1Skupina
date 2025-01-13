
class Kniha():

    def __init__(self, nazov, pocet_stran):         # inicializacna metoda/konštruktor
        self.set_nazov(nazov)                         
        self.set_pocet_stran(pocet_stran)

    def parametre_knihy(self):
        return f'Názov {self.nazov}, počet strán {self.pocet_stran}'

    def set_nazov(self, nazov):
        knihy = ['Zaklínač', 'Harry Potter', 'Pobrežie', 'Hory', 'Tatry']
        if nazov not in knihy:
            raise ValueError('chyba')
        else:
            self.nazov = nazov

    def set_pocet_stran(self, pocet):
        if pocet < 5 or pocet > 1000:
            raise ValueError('chyba nesplnate pocet')
        else:
            self.pocet_stran = pocet




kniha1 = Kniha('Zaklínač', 50)         # referencia na objekt/inštancia
kniha2 = Kniha('Harry Potter', 450)
kniha1.set_nazov('zak')
print(kniha1.nazov)

#print(kniha1.parametre_knihy())         # aplikovanie metody na objekt
#print(kniha1.pocet_stran)                # atribút
#print(kniha1.nazov)
#kniha1.pocet_stran = 380




        