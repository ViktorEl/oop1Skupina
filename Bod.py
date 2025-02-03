import math


class Bod():

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)
    
    def set_x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError('chyba neciselne vstupy')
        else:
            self.x = x

    def set_y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError('chyba neciselne vstupy')
        else:
            self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y

    def vzdialenost_od_bodu(self, other):
        if isinstance(other, Bod):
            vzdialenost = math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
            return vzdialenost
        else:
            raise ValueError('chyba bod nie je bod')



bod_a = Bod(6, 4)
bod_b = Bod(10, 6)

print(bod_a.vzdialenost_od_bodu(bod_b))    # 2.82