from bankovy_ucet import BankovyUcet

class Banka():

    def __init__(self, nazov):
        self.nazov = nazov
        self.zoznam = []

    def zaloz_ucet(self, meno, suma=0):
        ucet = BankovyUcet(meno, suma)
        for objekt in self.zoznam:
            meno_majitela = objekt.majitel
            if meno_majitela == meno:
                raise ValueError('chyba take meno uz existuje')
        self.zoznam.append(ucet)



vub = Banka('vub')
vub.zaloz_ucet('Radovan')




        