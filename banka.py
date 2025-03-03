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
 
    def vyber_vsetko(self, meno):
        ucet = self.__najdi_ucet(meno)
        suma_na_ucte = ucet.get_zostatok()
        suma_na_vyplatenie = suma_na_ucte / 1.01
        ucet.vyber(suma_na_vyplatenie)
        poplatok_banke = suma_na_ucte - suma_na_vyplatenie
        self.__interny_ucet.vklad(poplatok_banke)
        ucet.vyber(poplatok_banke)

    def prevod(self, meno_odosielatel, meno_prijemca, suma):
        ucet_odosielatel = self.__najdi_ucet(meno_odosielatel)
        ucet_prijemca = self.__najdi_ucet(meno_prijemca)
        zostatok_odosielatel = ucet_odosielatel.get_zostatok()
        suma_s_poplatkom = suma * 1.01
        if suma_s_poplatkom > zostatok_odosielatel:
            raise ValueError('chyba nemate dostatok financii na prevod')
        ucet_prijemca.vklad(suma)
        self.__interny_ucet.vklad(suma_s_poplatkom - suma)
        ucet_odosielatel.vyber(suma_s_poplatkom)
  
    




vub = Banka('vub')
vub.zaloz_ucet('Radovan')
vub.zrus_ucet('Radovan')




        