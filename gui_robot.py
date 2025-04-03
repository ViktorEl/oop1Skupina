from robot import Robot
import tkinter


class GUI(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title('Robot')
        self.geometry('600x400')
        self.robot = Robot('Jozo', 'Zelezo')
        self.prostredie()
        self.mainloop()


    def prostredie(self):
        tkinter.Button(self, text="Pozdrav sa", font=('Arial', 15), command=self.vypis_pozdrav).place(x=10, y=10)
        self.pozdravenie = tkinter.StringVar()
        tkinter.Entry(self, textvariable=self.pozdravenie, font=('Arial', 15)).place(x=150, y=15)

        tkinter.Button(self, text="Vymaz", font=("Arial", 15), command=self.vymaz_pozdrav).place(x=380, y=15)


    def vypis_pozdrav(self):
        self.pozdravenie.set(self.robot.pozdrav())

    def vymaz_pozdrav(self):
        self.pozdravenie.set('')


GUI()
