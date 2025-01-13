
class Kniha():

    def __init__(self, nazov, pocet_stran):         # inicializacna metoda/konštruktor
        self.nazov = nazov                          # inštančná premenná
        self.pocet_stran = pocet_stran

    def parametre_knihy(self):
        return f'Názov {self.nazov}, počet strán {self.pocet_stran}'



kniha1 = Kniha('Zaklináč', 350)         # referencia na objekt/inštancia
kniha2 = Kniha('Harry Potter', 450)

#print(kniha1.parametre_knihy())         # aplikovanie metody na objekt
print(kniha1.pocet_stran)                # atribút
print(kniha1.nazov)
kniha1.pocet_stran = 380




        