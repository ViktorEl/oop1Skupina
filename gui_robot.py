from robot import Robot
import tkinter


class GUI(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title('Robot')
        self.geometry('600x400')
        self.robot = Robot('Jozo', 'Zelezo')
        self.canvas = tkinter.Canvas(self, width=200, height=200)
        self.canvas.place(x=400, y=200)
        self.obrazok = tkinter.PhotoImage(file='robot.png')
        self.prostredie()
        self.mainloop()


    def prostredie(self):
        tkinter.Button(self, text="Pozdrav sa", font=('Arial', 15), command=self.vypis_a_nakresli).place(x=10, y=10)
        self.pozdravenie = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.pozdravenie, font=('Arial', 15)).place(x=150, y=15)

        tkinter.Button(self, text="Vymaz", font=("Arial", 15), command=self.vymaz_pozdrav).place(x=380, y=15)

        tkinter.Button(self, text="Material", font=('Arial', 15), command=self.vypis_material).place(x=10, y=70)
        self.matros = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.matros, font=('Arial', 15)).place(x=150, y=70)

        tkinter.Button(self, text="Vymaz", font=("Arial", 15), command= lambda: self.matros.set('')).place(x=380, y=70)

        tkinter.Button(self, text="Ukonči", font=("Arial", 15), background="red", fg="white", command=self.ukonci).place(x=10, y=300)

        tkinter.Label(self, text="Zadajte meno:", font=("Arial", 15)).place(x=10, y=130)
        self.zmena_mena = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.zmena_mena, font=("Arial", 15)).place(x=150, y=130)
        tkinter.Button(self, text="Zmeň meno", font=("Arial", 15), background="lightblue", command=self.zmen_meno).place(x=390, y=125)



    def vypis_pozdrav(self):
        self.pozdravenie.set(self.robot.pozdrav())

    def vymaz_pozdrav(self):
        self.pozdravenie.set('')
        self.canvas.delete('all')

    def vypis_material(self):
        self.matros.set(self.robot.matros())

    def zobraz_obrazok(self):
        self.canvas.create_image(120, 120, anchor=tkinter.CENTER, image=self.obrazok)

    def vypis_a_nakresli(self):
        self.vypis_pozdrav()
        self.zobraz_obrazok()

    def ukonci(self):
        self.destroy()

    def zmen_meno(self):
        meno_zmenene = self.zmena_mena.get()
        self.robot.meno = meno_zmenene

GUI()
