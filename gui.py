from Tkinter import *
from tkMessageBox import *
from teste import *

class Menu:
    def __init__(self, master):
        self.master = master
        self.master.title("Restaurante")
        kont = Controlador()
        self.topframe = Frame(self.master, bg='orange')
        self.topframe.pack()
        self.dados = Label(self.topframe, text='Restaurante JL',fg='black',bg='white',font=('Times','18','italic'))
        self.cadastracliente = Button(self.topframe, text='Registrar Cliente',fg='white', bg='orange',font=('Times','14'),command=self.chamada_primeiro)
        self.cadastrafuncionario = Button(self.topframe, text='Cadastrar Funcionario',fg='white', bg='orange',font=('Times','14'),command=self.chamar_segundo)
        self.registraumprato = Button(self.topframe, text='Registrar um Prato',fg='white', bg='orange',font=('Times','14'),command=self.chamar_terceiro)
        self.registraumareserva = Button(self.topframe, text='Registrar uma Reserva',fg='white', bg='orange',font=('Times','14'),command=self.chamar_quarto)
        self.historico = Button(self.topframe, text='Ver historico',fg='white', bg='orange',font=('Times','14'),command=self.chamar_quinto)
        self.verlucro = Button(self.topframe, text='Ver Lucro',fg='white', bg='orange',font=('Times','14'),command=self.chamar_sexto)
        self.criarmesa = Button(self.topframe, text='Criar uma mesa',fg='white', bg='orange',font=('Times','14'),command=self.chamar_oitavo)
        self.registrapedido = Button(self.topframe, text='Registrar um pedido',fg='white', bg='orange',font=('Times','14'),command=self.chamar_nono)
        self.dados.grid(row=0)
        self.cadastracliente.grid(row=3)
        self.cadastrafuncionario.grid(row=4)
        self.registraumprato.grid(row=5)
        self.registraumareserva.grid(row=6)
        self.historico.grid(row=7)
        self.verlucro.grid(row=9)
        self.criarmesa.grid(row=10)
        self.registrapedido.grid(row=11)


        
    def chamada_primeiro(self):
        a = Primeiro()

    def chamar_segundo(self):
        a = Segundo()

    def chamar_terceiro(self):
        a = Terceiro()

    def chamar_quarto(self):
        a = Quarto()

    def chamar_quinto(self):
        a = Quinto()

    def chamar_sexto(self):
        a = Sexto()

    def chamar_oitavo(self):
        a = Oitavo()

    def chamar_nono(self):
        a = Nono()


class Primeiro:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Cadastrar Cliente")
        kont = Controlador()
        self.frame = Frame(self.janela)
        self.frame.pack()
        self.labbel1 = Label(self.frame, text="Digite o nome").grid(row=10, sticky=E)
        self.entrada1 = Entry(self.frame)
        self.entrada1.grid(row=20, sticky=E)
        self.labbel2 = Label(self.frame, text="Digite a data de visita").grid(row=30, sticky=E)
        self.entrada2 = Entry(self.frame)
        self.entrada2.grid(row=40, sticky=E)
        self.labbel3 = Label(self.frame, text="Digite o ID").grid(row=50, sticky=E)
        self.entrada3 = Entry(self.frame)
        self.entrada3.grid(row=60, sticky=E)
        self.kadastro = Button(self.frame, text="Cadastrar", command=self.cadastro_cliente).grid(row=70, sticky=S)
        self.janela.mainloop

    def cadastro_cliente(self):
        kont = Controlador()
        nome = self.entrada1.get()
        data_visita = self.entrada2.get()
        id1 = self.entrada3.get()
        u = kont.cadastra_cliente(nome, data_visita, id1)
        g = kont.salvar_cliente()
        self.janela.destroy()


class Segundo:
    def __init__(self):
        self.janela7 = Tk()
        self.label_1 = Label(self.janela7, text='Email')
        self.label_2 = Label(self.janela7, text='')
        self.entry_1 = Entry(self.janela7)
        self.entry_2 = Entry(self.janela7, show='*')
        self.butao = Button(self.janela7, text="Enviar", command=self.chamar_login)
        self.label_1.grid(row=1, sticky=E)
        self.label_2.grid(row=2, sticky=E)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)
        self.butao.grid(row=3, column=1)
        self.janela7.mainloop()
        

    def login_cadastrar_funcionario(self):
        self.janela2 = Tk()
        self.janela2.title("Cadastrar Funcionario")
        kont = Controlador()
        self.el1 = Label(self.janela2, text="Digite o nome do Funcionario:").grid(row=10, sticky=W)
        self.entrada1 = Entry(self.janela2)
        self.entrada1.grid(row=20, sticky=E)
        self.labbel2 = Label(self.janela2, text="Digite a funçao do Funcionario:").grid(row=30, sticky=W)
        self.entrada2 = Entry(self.janela2)
        self.entrada2.grid(row=40, sticky=E)
        self.labbel3 = Label(self.janela2, text="Digite o salario do Funcionario:").grid(row=50, sticky=W)
        self.entrada3 = Entry(self.janela2)
        self.entrada3.grid(row=60, sticky=E)
        self.labbel3 = Label(self.janela2, text="Digite o ID do Funcionario").grid(row=70, sticky=W)
        self.entrada4 = Entry(self.janela2)
        self.entrada4.grid(row=80, sticky=E)
        self.labbel3 = Label(self.janela2, text="Digite o email do Funcionario").grid(row=90, sticky=W)
        self.entrada5 = Entry(self.janela2)
        self.entrada5.grid(row=100, sticky=E)
        self.labbel3 = Label(self.janela2, text="Digite a senha do Funcionario").grid(row=110, sticky=W)
        self.entrada6 = Entry(self.janela2)
        self.entrada6.grid(row=120, sticky=E)
        self.kadastro = Button(self.janela2, text="Cadastrar", command=self.cadastro_funcionario).grid(row=130, sticky=S)
        self.janela2.mainloop()



    def chamar_login(self):
        kont = Controlador()
        a = self.entry_1.get()
        b = self.entry_2.get()
        h = kont.login(a, b)
        if h == True:
            i = self.login_cadastrar_funcionario()
            self.janela7.destroy()
        else:
            j = self.erro
            
    def cadastro_funcionario(self):
        kont = Controlador()
        nome = self.entrada1.get()
        funcao = self.entrada2.get()
        salario = self.entrada3.get()
        idcliente = self.entrada4.get()
        email = self.entrada5.get()
        senha = self.entrada6.get()
        u = kont.cadastrando_funcionario(nome, funcao, salario, idcliente, email, senha)
        g = kont.salvar_funcionario()
        self.janela2.destroy()

    def erro(self):
        tk1 = Tk()
        kont = Controlador()
        labbel1 = Label(tk1, text="Gerente não encontrado, tente novamente").grid(row=10, sticky=N)
        butao = Button(tk1, text="Ok", command=self.destruir)
        butao.grid(row=20, sticky=S)
        tk1.mainloop()

    def destruir(self):
        tk1.destroy()

class Terceiro:
    def __init__(self):
        self.janela3 = Tk()
        self.janela3.title("Cadastrar Prato")
        kont = Controlador()
        self.labbel1 = Label(self.janela3, text="Digite o nome do Prato:").grid(row=10, sticky=W)
        self.entrada1 = Entry(self.janela3)
        self.entrada1.grid(row=20, sticky=E)
        self.labbel2 = Label(self.janela3, text="Digite o valor do Prato:").grid(row=30, sticky=W)
        self.entrada2 = Entry(self.janela3)
        self.entrada2.grid(row=40, sticky=E)
        self.kadastro = Button(self.janela3, text="Cadastrar", command=self.cadastro_prato).grid(row=130, sticky=S)
        self.janela3.mainloop()

    def cadastro_prato(self):
        kont = Controlador()
        nome_prato = self.entrada1.get()
        valor_prato = self.entrada2.get()
        U = kont.cadastra_prato(nome_prato, valor_prato)
        G = kont.salvar_prato()
        self.janela3.destroy()

class Quarto:     
    def __init__(self):
        self.janela4 = Tk()
        self.janela4.title("Cadastrar Reserva")
        kont = Controlador()
        self.labbel1 = Label(self.janela4, text="Digite o nome do cliente que fez a reserva:").grid(row=10, sticky=W)
        self.entrada1 = Entry(self.janela4)
        self.entrada1.grid(row=20, sticky=E)
        self.labbel2 = Label(self.janela4, text="Digite o numero da mesa:").grid(row=30, sticky=W)
        self.entrada2 = Entry(self.janela4)
        self.entrada2.grid(row=40, sticky=E)
        self.labbel3 = Label(self.janela4, text="Digite a data da reserva:").grid(row=50, sticky=W)
        self.entrada3 = Entry(self.janela4)
        self.entrada3.grid(row=60, sticky=E)
        self.labbel3 = Label(self.janela4, text="Digite a hora da reserva:").grid(row=70, sticky=W)
        self.entrada4 = Entry(self.janela4)
        self.entrada4.grid(row=90, sticky=E)
        self.kadastro = Button(self.janela4, text="Cadastrar", command=self.registrar_reserva).grid(row=130, sticky=S)
        self.janela4.mainloop()



    def registrar_reserva(self):
        kont = Controlador()
        nome = self.entrada1.get()
        numero = self.entrada2.get()
        data = self.entrada3.get()
        hora = self.entrada4.get()
        U = kont.definindo_uma_reserva(nome, numero, data, hora)
        G = kont.salvar_reserva()
        self.janela4.destroy()

class Quinto:
    def __init__(self):
        janela5 = Tk()
        kont = Controlador()
        janela5.title('Historico')
        janela5.geometry('400x197')
        for k in range(len(kont.lista_pedidos)):
            a = str(kont.lista_pedidos[k])
            

        janela5.mainloop()
        

class Sexto:
    def __init__(self):
        kont = Controlador()
        janela6 = Tk()
        janela6.title("Saber Lucro")
        h = kont.saber_lucro()
        t = Text(janela6)
        t.insert(END, h)
        t.pack()
            
        janela6.mainloop

class Setimo:
    def __init__(self):
        self.janela7 = Tk()
        self.label_1 = Label(self.janela7, text='Email')
        self.label_2 = Label(self.janela7, text='')
        self.entry_1 = Entry(self.janela7)
        self.entry_2 = Entry(self.janela7, show='*')
        self.label_1.grid(row=1, sticky=E)
        self.label_2.grid(row=2, sticky=E)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)
        self.janela7.mainloop()

class Oitavo:
    def __init__(self):
        self.janela8 = Tk()
        self.janela8.title("Cadastrar Mesa")
        kont = Controlador()
        self.labbel1 = Label(self.janela8, text="Digite o numero da mesa:").grid(row=10, sticky=W)
        self.entrada1 = Entry(self.janela8)
        self.entrada1.grid(row=20, sticky=E)
        self.labbel2 = Label(self.janela8, text="Digite a disponibilidade da mesa:").grid(row=30, sticky=W)
        self.entrada2 = Entry(self.janela8)
        self.entrada2.grid(row=40, sticky=E)
        self.kadastro = Button(self.janela8, text="Cadastrar", command=self.cadastro_mesa).grid(row=130, sticky=S)
        self.janela8.mainloop


    def cadastro_mesa(self):
        kont = Controlador()
        numero =  self.entrada1.get()
        disponibilidade = self.entrada2.get()
        U = kont.criar_mesa(numero, disponibilidade)
        G = kont.salvar_mesa()
        self.janela8.destroy()


class Nono:
    def  __init__(self):
        self.janela9 = Tk()
        self.janela9.title("Registrar Pedido")
        kont = Controlador()
        self.labbel1 = Label(self.janela9, text="Digite a quantidade:").grid(row=10, sticky=W)
        self.entrada1 = Entry(self.janela9)
        self.entrada1.grid(row=20, sticky=E)
        self.labbel2 = Label(self.janela9, text="Digite o prato:").grid(row=30, sticky=W)
        self.entrada2 = Entry(self.janela9)
        self.entrada2.grid(row=40, sticky=E)
        self.labbel3 = Label(self.janela9, text="Digite o nome do cliente que pediu:").grid(row=50, sticky=W)
        self.entrada3 = Entry(self.janela9)
        self.entrada3.grid(row=60, sticky=E)
        self.kadastro = Button(self.janela9, text="Cadastrar", command=self.registro_pedido).grid(row=130, sticky=S)
        self.janela9.mainloop

    def registro_pedido(self):
        kont =  Controlador()
        quantidade = self.entrada1.get()
        prato = self.entrada2.get()
        nome = self.entrada3.get()
        U = kont.registra_pedido_cliente(quantidade, prato, nome)
        G = kont.salvar_pedido()
        self.janela9.destroy()



root = Tk()
janela = Menu(root)
root.mainloop()





        

            









