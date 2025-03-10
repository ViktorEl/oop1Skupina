
class Osoba():

    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def predstav_sa(self):
        return f'Moje meno je {self.meno} a mam {self.vek} rokov'
    






osoba1 = Osoba('Jozo', 15)