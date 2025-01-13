
class Kniha():

    def __init__(self, nazov, pocet_stran):         # inicializacna metoda/konštruktor
        self.nazov = nazov                          # inštančná premenná
        self.pocet_stran = pocet_stran

    def parametre_knihy(self):
        return f'Názov {self.nazov} a počet strán {self.pocet_stran}'


kniha1 = Kniha('Zaklináč', 350)         # referencia na objekt/inštancia
kniha2 = Kniha('Harry Potter', 450)



        