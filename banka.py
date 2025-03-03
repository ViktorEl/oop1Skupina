from bankovy_ucet import BankovyUcet

class Banka():

    def __init__(self, nazov):
        self.nazov = nazov
        self.zoznam = []

    def zaloz_ucet(self, meno, zostatok=0):
        ucet = BankovyUcet(meno, zostatok)
        for objekt in self.zoznam:
            meno_majitela = objekt.majitel
            if meno_majitela == meno:
                raise ValueError('chyba take meno uz existuje')
        self.zoznam.append(ucet)

    def zrus_ucet(self, meno):
        existuje_majitel = False
        nulovy_zostatok = False
        for objekt in self.zoznam:
            if objekt.majitel == meno:
                existuje_majitel = True
                if objekt.get_zostatok() == 0:
                    nulovy_zostatok =  True
                    self.zoznam.remove(objekt)
        if existuje_majitel == False:
            raise ValueError('Chyba klient neexistuje')
        if nulovy_zostatok == False:
            raise ValueError('chyba nemáte nulový zostatok')


    def __najdi_ucet(self, meno):
        existuje_ucet = False
        for objekt in self.zoznam:
            meno_majitela_uctu = objekt.majitel
            if meno_majitela_uctu == meno:
                existuje_ucet = True
                return objekt
        if not existuje_ucet:
            raise ValueError('chyba klient neexistuje')

    def vloz_na_ucet(self, meno, suma):

 





vub = Banka('vub')
vub.zaloz_ucet('Radovan')
vub.zrus_ucet('Radovan')




        