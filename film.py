
class Film():

    def __init__(self, nazov, rok, zaner):
        self.set_nazov(nazov)
        self.set_rok(rok)
        self.set_zaner(zaner)
    
    def set_nazov(self, nazov):
        if len(nazov) < 3:
            raise ValueError('chyba kratky nazov')
        else:
            self.nazov = nazov
    
    def set_rok(self, rok):
        typ = type(rok)
        if typ != int:
            raise ValueError('chyba rok musi byt cislo')
        if rok < 1888:
            raise ValueError('chyba neexistujuci rok')
        else:
            self.rok = rok

    def set_zaner(self, zaner):
        zoznam = ['akčný', 'triler', 'horor', 'romantický', 'dráma',
                  'animovaný', 'biografický', 'sci-fi', 'dobrodružný']
        if zaner not in zoznam:
            raise ValueError('chyba taky zaner neexistuje')
        else:
            self.zaner = zaner
    
    def vypis_film(self):
        print(f'Názov filmu: {self.nazov}, Rok natočenia: {self.rok}, Žáner: {self.zaner}')

            
#film1 = Film('a', 1998, 'akčný')               # chyba krátky názov
#film2 = Film('Rýchlo a zbesilo', 5, 'akčný')   # chyba rok
#film3 = Film('Rýchlo a zbesilo', 'aa', 'akčný') # chyba rok nie je cislo
#film4 = Film('Rýchlo a zbesilo', 2001, 'n')      # chyba zanru
film5 = Film('Rýchlo a zbesilo', 2001, 'akčný') # správny objekt
film5.vypis_film()

