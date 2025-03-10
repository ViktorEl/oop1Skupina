
class Osoba():

    def __init__(self, meno, vek):
        self.meno = meno
        self.vek = vek

    def predstav_sa(self):
        return f'Moje meno je {self.meno} a mam {self.vek} rokov'
    
class Student(Osoba):                           #dedenie z triedy Osoba

    def __init__(self, meno, vek, rocnik):
        super().__init__(meno, vek)             # dedenie atributov
        self.rocnik = rocnik                    # vytvorenie noveho atributu

    def predstav_sa(self):
        return super().predstav_sa() + f' a navstevujem {self.rocnik}' # prepisanie metody / polymorfizmus
    

class Ucitel(Osoba):

    def __init__(self, meno, vek, predmet):
        super().__init__(meno, vek)
        self.predmet = predmet

    def predstav_sa(self):
        return super().predstav_sa() + f' ucim predmet {self.predmet}'


class Asistent(Student):

    def __init__(self, meno, vek, rocnik, predmet):
        super().__init__(meno, vek, rocnik)
        self.predmet = predmet

    def predstav_sa(self):
        return super().predstav_sa() + f' som zaroven asistentom a ucim predmet {self.predmet}'







osoba1 = Osoba('Jozo', 15)
student1 = Student('Jano', 18, '4.rocnik')
#print(student1.predstav_sa())
ucitel1 = Ucitel('Fero', 39, 'SJL')
#print(ucitel1.predstav_sa())
asistent1 = Asistent('Adam', 19, '2.rocnik', 'MAT')
print(asistent1.predstav_sa())