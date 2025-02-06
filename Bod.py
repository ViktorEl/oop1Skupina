import math

class Bod():

    def __init__(self, x, y):
        self.set_x(x)
        self.set_y(y)
    
    def __set_x(self, x):
        if not isinstance(x, (int, float)):
            raise ValueError('chyba neciselne vstupy')
        else:
            self.__x = x

    def __set_y(self, y):
        if not isinstance(y, (int, float)):
            raise ValueError('chyba neciselne vstupy')
        else:
            self.__y = y

    def __get_x(self):
        return self.__x
    
    def __get_y(self):
        return self.__y

    def vzdialenost_od_bodu(self, other):
        if isinstance(other, Bod):
            vzdialenost = math.sqrt((self.__get_x() - other.__get_x())**2 + (self.__y - other.__y)**2)
            return vzdialenost
        else:
            raise ValueError('chyba bod nie je bod')


    def vzdialenost_od_pociatku(self):
        vzdialenost = self.vzdialenost_od_bodu(Bod(0,0))
        return vzdialenost

    def __eq__(self, other):
        if isinstance(other, Bod):
            if self.__x == other.__x and self.__y == other.__y:
                return True
            return False
        return False

    def __str__(self):
        return f'{self.__x} {self.__y}'

    x = property(__get_x, __set_x)
    y = property(__get_y, __set_y)


bod_a = Bod(6, 4)
bod_b = Bod(10, 6)

print(bod_a.vzdialenost_od_bodu(bod_b))    
print(bod_a.vzdialenost_od_pociatku())      #7,2111
print(bod_a == bod_b)                       # pouzitie magickej metody eq
print(bod_a)
