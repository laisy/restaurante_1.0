from Tkinter import *
from ttk import Notebook

class JanelaOpcoes:

    def __init__(self, master):

        self.principal = Notebook(master)
        
        self.frameA = Frame(self.principal, height=300, width=200)
        self.frameA.pack()
       
        self.frameB = Frame(self.principal, height=300, width=200)
        self.frameB.pack()

        self.frameC = Frame(self.principal, height=300, width=200)
        self.frameC.pack()

        self.frameD = Frame(self.principal, height=300, width=200)
        self.frameD.pack()

        self.frameE = Frame(self.principal, height=300, width=200)
        self.frameE.pack()

        self.principal.add(self.frameA, text='Clientes')
        self.principal.add(self.frameB, text='Pratos')
        self.principal.add(self.frameC, text='Mesas')
        self.principal.add(self.frameD, text='Pedidos')
        self.principal.add(self.frameE, text='Reservas')
        
        
        self.principal.pack()        


root = Tk()
p = JanelaOpcoes(root)
root.mainloop()

