from Tkinter import *
from tkMessageBox import *

class nada_selecionado(Exception):
    pass

class JanelaPrograma:

    def __init__(self, janela):
        self.frame = Frame(janela, height=200, width=300)
        self.frame.pack()

        self.labeloperacao = Label(self.frame, text = 'Escolha sua opção:')
        self.labeloperacao.place(x=0,y=70)

        self.var_gerente = IntVar()
        self.checkgerente = Checkbutton(self.frame, text='Gerente', variable = self.var_gerente)
        self.checkgerente.place(x=0,y=100)
        flag1 = False

        self.var_funcionario = IntVar()
        self.checkfuncionario = Checkbutton(self.frame, text='Funcionário', variable = self.var_funcionario)
        self.checkfuncionario.place(x=0,y=120)
        flag2 = False

        self.button_iniciar = Button(self.frame, text='Iniciar', height=1, width=20,command=self.iniciar)
        self.button_iniciar.place(x=5,y=150)

       

    def iniciar(self):
        try:
            
            if self.checkgerente == False and self.checkfuncionario == False:
                raise nada_selecionado
            if self.checkgerente == True and self.checkfuncionario == True:
                raise nada_selecionado

            root.destroy()
            janela = Tk()
            janela.geometry("300x200")
        
            self.label_1 = Label(janela, text='Login')
            self.label_2 = Label(janela, text='Senha')
    
            self.entry_1 = Entry(janela)
            self.entry_2 = Entry(janela, show='*')
        
            self.label_1.grid(row=10, sticky=E)
            self.label_2.grid(row=15, sticky=E)
        
            self.entry_1.grid(row=10, column=1)
            self.entry_2.grid(row=15, column=1)

            c = Checkbutton(janela, text='Lembrar-me')
            c.grid(columnspan=2)

            b = Button(janela, text='Enviar')
            b.grid(columnspan=10)
        
            janela.mainloop()

        except nada_selecionado:
            showerror('Error', 'Selecione apenas uma')

    

root = Tk()
p = JanelaPrograma(root)
root.mainloop()
