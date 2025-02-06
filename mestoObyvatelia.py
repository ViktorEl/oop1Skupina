from obyvatel import Obyvatel


class MestoObyvatelia():

    def __init__(self, mesto):
        self.mesto = mesto
        self.obyvatelia = []

    def uloz_obyvatela(self, meno, vek, pohlavie):
        obyvatel = Obyvatel(meno, vek, pohlavie)
        self.obyvatelia.append(obyvatel)


mesto1 = MestoObyvatelia('Roznava')

mesto1.uloz_obyvatela('Jozo', 15, 'm')
