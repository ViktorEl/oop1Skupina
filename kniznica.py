from kniha2 import Kniha


class Kniznica():

    def __init__(self, meno):
        self.set_meno(meno)
        self.zoznam = []

    def set_meno(self, meno):
        if len(meno) > 20:
            raise ValueError('chyba dlhe meno kniznice')
        self.meno = meno

    def uloz_knihu(self, nazov, suma):
        kniha = Kniha(nazov, suma)
        self.zoznam.append(kniha)

    def vypis_knihy(self):
        retazec = ''
        for kniha in self.zoznam:
            retazec += kniha.get_nazov() + '\n'
        return retazec
    
    def celkova_hodnota_knih(self):
        spolu_suma = 0
        for kniha in self.zoznam:
            spolu_suma += kniha.get_suma()
        spolu_suma =  str(round(spolu_suma, 2)) + '0'
        return spolu_suma

            
kniznica = Kniznica('Betliar')
kniznica2 = Kniznica('Roznava')

kniznica.uloz_knihu('Zaklinac', 19.90)
kniznica.uloz_knihu('Harry Potter', 15.70)
print(kniznica.vypis_knihy())
print(kniznica.celkova_hodnota_knih())


