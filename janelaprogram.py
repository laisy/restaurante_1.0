from Tkinter import *
from tkMessageBox import *
from teste import *

kont = Controlador()

class Login:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurante")
        label_1 = Label(self.master, text='Login').grid(row=10, sticky=E)
        label_2 = Label(self.master, text='Senha').grid(row=15, sticky=E)
        self.usuario = entry_1 = Entry(self.master).grid(row=10, column=1)
        self.senha = entry_2 = Entry(self.master, show='*').grid(row=15, column=1)
        b = Button(self.master, text='Enviar', command=self.proucura_login(self.usuario, self.senha)).grid(columnspan=10)
        if b == True:
            print "deu"
        else:
            print "n deu"

    def proucura_login(self, t1, t2):
        flag = False
        for i in range(len(kont.lista_funcionario)):
            if t1 == kont.lista_funcionario[i]:
                if t2 == kont.lista_funcionario[i]:
                    flag = True
                    return flag
                    
        


root = Tk()
Login(root)
root.mainloop()
