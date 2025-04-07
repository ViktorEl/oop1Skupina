class Robot():

    def __init__(self, meno, material):
        self.set_meno(meno)
        self.material = material

    def pozdrav(self):
        return f'Volám sa {self.meno}'
    
    def matros(self):
        return f'Som vyrobeny z {self.material}'
    
    def set_meno(self, meno):
        if not meno.isalpha():
            raise ValueError("Chyba musite zadat len znaky abecedy")
        self.meno = meno