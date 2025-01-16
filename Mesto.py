
class Mesto:

    def __init__(self, nazov, pocet, rozloha):
        self.set_pocet(pocet)
        self.set_rozloha(rozloha)
        self.nazov = nazov

    def set_pocet(self, pocet):
        if pocet < 0:
            raise ValueError('chyba zaporne cislo')
        else:
            self.__pocet = pocet

    def set_rozloha(self, rozloha):
        if rozloha < 0:
            raise ValueError('chyba zaporne cislo')
        else:
            self.__rozloha = rozloha
    

mesto1 = Mesto('Rožňava', 20000, 45.61)