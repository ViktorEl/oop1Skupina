import datetime


'''kontrola datumu'''



rok = 88
mesiac = 3
den = 6

try:
    datetime.datetime(rok, mesiac, den)
    print('korektny datum')
except ValueError:
    raise ValueError('chyba nekorektny datum')

'''MUZ'''
# pohlavie - ak je na tretej pozicii 0 alebo 1
# 050518 / 6781



'''ZENA'''
# zistenie pohlavia - ak je na tretej pozicii 5 alebo 6 tak je to žena
# zistenie mesiaca - tretia a stvrta pozicia je mesiac ale je k nemu pripocitane cislo 50
# zistenie mesiaca - napríklad ak je rodne cislo 885104 tak mesiac narodenia je 1 pretože 51 - 50 = 1
# 0555189811
# 2005
# 55 - 50 = 5
# den 18
