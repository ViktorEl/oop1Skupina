class Robot():

    def __init__(self, meno, material):
        self.meno = meno
        self.material = material

    def pozdrav(self):
        return f'Volám sa {self.meno}'
    
    def matros(self):
        return f'Som vyrobeny z {self.material}'