from obyvatel import Obyvatel


class MestoObyvatelia():

    def __init__(self, mesto):
        self.mesto = mesto
        self.obyvatelia = []

    def uloz_obyvatela(self, meno, vek, pohlavie):
        obyvatel = Obyvatel(meno, vek, pohlavie)
        self.obyvatelia.append(obyvatel)

    def spocitaj_obyvatelov_podla_veku(self, vek):
        pocitadlo = 0
        for obyvatel in self.obyvatelia:
            vek_obyvatela = obyvatel.get_vek()
            if vek_obyvatela == vek:
                pocitadlo += 1
        return pocitadlo

    def spocitaj_obyvatelov_podla_pohlavia(self, pohlavie):
        pocitadlo = 0
        for obyvatel in self.obyvatelia:
            pohlavie_obyvatela = obyvatel.get_pohlavie()
            if pohlavie_obyvatela == pohlavie:
                pocitadlo += 1
        return pocitadlo



mesto1 = MestoObyvatelia('Roznava')

mesto1.uloz_obyvatela('Jozo', 15, 'm')
mesto1.uloz_obyvatela('Jano', 15, 'm')
mesto1.uloz_obyvatela('Lucia', 18, 'z')
mesto1.uloz_obyvatela('Anna', 16, 'z')
mesto1.uloz_obyvatela('Milan', 19, 'm')

print(mesto1.spocitaj_obyvatelov_podla_veku(15))
print(mesto1.spocitaj_obyvatelov_podla_pohlavia('m'))