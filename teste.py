from mesa import *
from cliente import *
from prato import *
from pedidos import *
from funcionario import *
from login import *
from reserva import *

class Controlador:
    def __init__(self):
        self.lista_cliente = []
        arq1 = open("lista_clientes.txt", "r")
        for i in arq1:
            splitou = i.split(" ")
            a = self.cadastra_cliente(splitou[0], splitou[1], splitou[2])

        arq1.close()

        self.lista_funcionario = []
        arq2 = open("lista_funcionarios.txt", "r")
        for k in arq2:
            splitou2 = k.split(" ")
            b = self.cadastrando_funcionario(splitou2[0], splitou2[1], splitou2[2], splitou2[3], splitou2[4], splitou2[5])

        arq2.close()
       

        self.lista_pratos = []
        arq3 = open("lista_pratos.txt", "r")
        for h in arq3:
            splitou3 = h.split(" ")
            c = self.cadastra_prato(splitou3[0], splitou3[1])

        arq3.close()


        self.lista_pedidos = []
        arq4 = open("lista_pedidos.txt", "r")
        for j in arq4:
            splitou4 = j.split(" ")
            d = self.registra_pedido_cliente(splitou4[0], splitou4[1], splitou4[2])

        arq4.close()
        
        self.lista_nova_reserva = []
        arq5 = open("lista_reserva.txt", "r")
        for l in arq5:
            splitou5 = l.split(" ")
            f = self.definindo_uma_reserva(splitou5[0], splitou5[1], splitou5[2], splitou5[3])

        arq5.close()

        self.lista_mesa = []
        arq6 = open("lista_mesa.txt", "r")
        for p in arq6:
            splitou6 = p.split(" ")
            g = self.criar_mesa(splitou6[0], splitou6[1])

        arq6.close()
        


    def login(self, email, senha):
        flag = False
        for k in range(len(self.lista_funcionario)):
            if self.lista_funcionario[k].email_funcionario == email and self.lista_funcionario[k].senha_funcionario == senha:
                if self.lista_funcionario[k].funcao_exercida == "Gerente":
                    flag = True

        return flag
            


    def cadastra_cliente(self, nomeCliente, dataVisita, idCliente):
        novo_cliente = Cliente(nomeCliente, dataVisita, idCliente)
        self.lista_cliente.append(novo_cliente)

    def cadastra_prato(self, nomePrato, valorPrato):
        novo_prato = Prato(nomePrato, valorPrato)
        self.lista_pratos.append(novo_prato)

    def registra_pedido_cliente(self, quantidadePedida, pratoPedido, nomeCliente):
        pedido = Pedidos(quantidadePedida, pratoPedido, nomeCliente)
        self.lista_pedidos.append(pedido)


    def definindo_uma_reserva(self, nomeReservista, numeroMesa, dataReservada, horaReservada):
        nova_reserva = Reserva(nomeReservista, numeroMesa, dataReservada, horaReservada) 
        self.lista_nova_reserva.append(nova_reserva)

    def cadastrando_funcionario(self, nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario, emailFuncionario, senhaFuncionario):
        novo_funcionario = Funcionario(nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario, emailFuncionario, senhaFuncionario)
        self.lista_funcionario.append(novo_funcionario)

    def salvar_reserva(self, nomeReservista, numeroMesa, dataReserva, horaReserva):
        nova_reserva = Reserva(nomeReservista, numeroMesa, dataReserva, horaReserva)
        self.lista_nova_reserva.append(nova_reserva)

    def ver_pedidos(self):
        for i in range(len(self.lista_pedidos)):
            return self.lista_pedidos[i]
        
    def saber_lucro(self):
        ini = 0
        for i in range(len(self.lista)):
            if self.lista_pedidos == self.lista_pedidos[i].prato_pedido:
                for k in range(len(self.lista_pratos)):
                    if pratoPedido == self.lista_pratos[k].nome_do_prato:
                        ini += float(self.lista_pratos.valor_do_prato)

        for k in range(len(self.lista_funcionario)):
            fin = 0
            if self.lista_funcionario == Funcionario.salario_recebido:
                fin += float(Funcionario.salario_recebido)

            h = ini - fin
            return h

    def criar_mesa(self, numeroMesa, disponibiliMesa):
        m = Mesa(numeroMesa, disponibiliMesa)
        self.lista_mesa.append(m)

    def salvar_cliente(self):
        arquivo1 = open("lista_clientes.txt", "w")
        for k in range(len(self.lista_cliente)):
            arquivo1.write(str(self.lista_cliente[k].novo_cliente) + " ")
            arquivo1.write(str(self.lista_cliente[k].nova_visita) + " ") 
            arquivo1.write(str(self.lista_cliente[k].novo_id) + " \n")

        arquivo1.close()
       
    def salvar_prato(self):
        arquivo2 = open("lista_pratos.txt", "w")
        for k in range(len(self.lista_pratos)):
            arquivo2.write(str(self.lista_pratos[k].nome_do_prato) + " ")
            arquivo2.write(str(self.lista_pratos[k].valor_do_prato) + " \n")
 
        arquivo2.close()

    def salvar_pedido(self):
        arquivo3 = open("lista_pedidos.txt", "w")
        for k in range(len(self.lista_pedidos)):
            arquivo3.write(str(self.lista_pedidos[k].quantidade_vendida) + " ")
            arquivo3.write(str(self.lista_pedidos[k].prato_pedido) + " ")
            arquivo3.write(str(self.lista_pedidos[k].cliente_pediu) + " \n")

 
        arquivo3.close()

    def salvar_reserva(self):
        arquivo4 = open("lista_reserva.txt", "w")
        for k in range(len(self.lista_nova_reserva)):
            arquivo4.write(str(self.lista_nova_reserva[k].nome_reservou) + " ")
            arquivo4.write(str(self.lista_nova_reserva[k].numero_mesa) + " ")
            arquivo4.write(str(self.lista_nova_reserva[k].data_reservada) + " ")
            arquivo4.write(str(self.lista_nova_reserva[k].hora_reservada) + " \n")
            
        arquivo4.close()

    def salvar_funcionario(self):
         arquivo5 = open("lista_funcionarios.txt", "w")
         for k in range(len(self.lista_funcionario)):
             arquivo5.write(str(self.lista_funcionario[k].nome_funcionario) + " " )
             arquivo5.write(str(self.lista_funcionario[k].funcao_exercida) + " " )
             arquivo5.write(str(self.lista_funcionario[k].salario_recebido) + " " )
             arquivo5.write(str(self.lista_funcionario[k].codigo_funcionario) + " ")
             arquivo5.write(str(self.lista_funcionario[k].email_funcionario) + " ")
             arquivo5.write(str(self.lista_funcionario[k].senha_funcionario)+ " \n")
 

         arquivo5.close()

    def salvar_mesa(self):
        arquivo6 = open("lista_mesa.txt", "w")
        for i in range(len(self.lista_mesa)):
            arquivo6.write(str(self.lista_mesa[i].numero_mesa) + " ")
            arquivo6.write(str(self.lista_mesa[i].disponibilidade_mesa) + " ")

        arquivo6.close()
            

 
         
