

class BankovyUcet():

    def __init__(self, majitel, zostatok=0):
        self.set_majitel(majitel)
        self.__zostatok = zostatok

    def set_majitel(self, majitel):
        if len(majitel) < 1:
            raise ValueError('chyba meno majitela nemoze byt prazdne')
        else:
            self.__majitel = majitel

    def vklad(self, suma):
        if not isinstance(suma, (int, float)):
            raise ValueError('Chyba museli ste zadat neciselny znak')
        self.__zostatok += suma

    def vyber(self, suma):
        if not isinstance(suma, (int, float)):
            raise ValueError('Chyba museli ste zadat neciselny znak')
        if suma > self.__zostatok:
            raise ValueError('Nemate dostatok penazi na ucte')
        self.__zostatok -= suma

    def __str__(self):
        return f'{self.__majitel} {self.__zostatok}'

    def __get_majitel(self):
        return self.__majitel
    
    majitel = property(__get_majitel)


daniel = BankovyUcet('Daniel')  # zalozenie uctu
daniel.vklad(60)
daniel.vyber(20)
daniel.vyber(13.80)
print(daniel.majitel)
print(daniel)


        