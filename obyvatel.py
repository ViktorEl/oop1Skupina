

class Obyvatel():

    def __init__(self, meno, vek, pohlavie):
        self.set_meno(meno)
        self.set_vek(vek)
        self.set_pohlavie(pohlavie)

    def set_meno(self, meno):
        if not isinstance(meno, str):
            raise ValueError('chyba meno musi byt string')
        if meno == '':
            raise ValueError('chyba musite zadate meno')
        if not meno.isalpha():
            raise ValueError('chyba asi ste zadali nekorektne znaky')
        if len(meno)  < 3:
            raise ValueError('chyba kratke meno')
        self.meno = meno

    def set_pohlavie(self, pohlavie):
        list = ['z', 'm']
        if pohlavie not in list:
            raise ValueError('chyba nespravne pohlavie')
        self.pohlavie = pohlavie
    
    def set_vek(self, vek):
        if not isinstance(vek, int):
            raise ValueError('chyba vek musi byt cislo')
        if vek < 0 or vek > 150:
            raise ValueError('chyba nespravny vek')
        self.vek = vek



clovek1 = Obyvatel('Jano')
#clovek1.set_meno(15)           # kontrola stringu
#clovek1.set_meno('Jano85')      # kontrola len znakov abecedy
#clovek1.set_meno('')            # prazdne
#clovek1.set_meno('Ja')           # kratke meno


