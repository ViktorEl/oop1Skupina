from bankovy_ucet import BankovyUcet

class Banka():

    def __init__(self, nazov):
        self.nazov = nazov
        self.zoznam = []
        self.__interny_ucet = BankovyUcet(nazov, zostatok=0)

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
        ucet = self.__najdi_ucet(meno)
        ucet.vklad(suma)

    def vyber_z_uctu(self, meno, suma):
        ucet = self.__najdi_ucet(meno)
        zostatok_na_ucte = ucet.get_zostatok()
        suma_s_poplatkom = suma * 1.01
        if suma_s_poplatkom > zostatok_na_ucte:
            raise ValueError('chyba nemate dostatok penazi')
        else:
            ucet.vyber(suma)
            poplatok = suma_s_poplatkom - suma
            self.__interny_ucet.vklad(poplatok)
            ucet.vyber(poplatok)
 





vub = Banka('vub')
vub.zaloz_ucet('Radovan')
vub.zrus_ucet('Radovan')




        