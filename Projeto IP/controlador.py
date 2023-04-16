from mesa import *
from cliente import *
from prato import *
from pedidos import *
from reserva import *
from funcionario import *
from login import *

class Controlador:
    def __init__(self):
        self.lista_cliente = []
        arq1 = open("lista_clientes.txt", "r")        
        for i in (arq1):
            splitou = i.split()
            cliente = Cliente(splitou[0], splitou[1], splitou[2])
            self.lista_cliente.append(cliente)


        arq1.close()

        self.lista_login = []
        arq7 = open("lista_login.txt", "r")
        for i in (arq7):
            splitou = i.split()
            login = Login(splitou[0], splitou[1])
            self.lista_login.append(login)

        arq7.close()
        
        self.lista_funcionario = []
        arq2 = open("lista_funcionarios.txt", "r")
        for i in (arq2):
            splitou = i.split()
            funcionario = Funcionario(splitou[0], splitou[1], splitou[2], splitou[3])
            self.lista_funcionario.append(funcionario)

        arq2.close()

        self.lista_pratos = []
        arq3 = open("lista_pratos.txt", "r")
        for i in (arq3):
            splitou = i.split()
            prato = Prato(splitou[0], splitou[1])
            self.lista_pratos.append(prato)
            
        arq3.close()
        
        self.lista_pedidos_dia = []
        arq4 = open("lista_pedidos.txt", "r")
        for i in (arq4):
            splitou = i.split
            pedido = Pedidos(splitou[0], splitou[1], splitou[2], splitou[3], splitou[4])
            self.lista_pedidos.append(pedido)
 
        arq4.close()

        self.lista_lucro = []
        self.lista_nova_reserva = []
        arq5 = open("lista_reservas.txt", "r")
        for i in (arq5):
            splitou = i.split()
            reserva = splitou[0], splitou[1], splitou[3]
            self.lista_nova_reserva.append(reserva)

        arq5.close()

    def cadastra_cliente(self, nomeCliente, dataVisita, idCliente):
        novo_cliente = Cliente(nomeCliente, dataVisita, idCliente)
        self.lista_cliente.append(novo_cliente)

    def cadastra_prato(self, nomePrato, valorPrato):
        novo_prato = Prato(nomePrato, valorPrato)
        self.lista_pratos.append(novo_prato)

    def registra_pedido_cliente(self, quantidadePedida, pratoPedido, nomeCliente, numeroMesa, disponibilidadeMesa):
        pedido = Pedido(quantidadePedida, pratoPedido, nomeCliente)
        mesa_pedida = Mesa(numeroMesa, disponibilidadeMesa)
        self.lista_pedidos_dia.append(pedido)
        self.lista_pedidos_dia.append(mesa_pedida)

    def definindo_uma_reserva(self, nomeReservista, numeroMesa, dataReservada, horaReservada):
        nova_reserva = Reserva(nomeReservista, numeroMesa, dataReservada, horaReservada) 
        self.lista_nova_reserva.append(nova_reserva)

    def cadastrando_funcionario(self, nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario, senhaFuncionario, emailFuncionario):
        novo_funcionario = Funcionario(nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario)
        novo_login = Login(senhaFuncionario, emailFuncionario)
        self.lista_funcionario.append(novo_funcionario)
        self.lista_login.append(novo_login)
        

    def salvar_cliente(self):
        arquivo1 = open("lista_clientes.txt", "w")
        for k in range(len(self.lista_cliente)):
            arquivo1.write(str(self.lista_cliente[k].novo_cliente)) + " "
            arquivo1.write(str(self.lista_cliente[k].nova_visita)) + " "
            arquivo1.write(str(self.lista_cliente[k].novo_numero_cliente)) + "/n"

        arquivo1.close()

    def salvar_prato(self):
        arquivo2 = open("lista_pratos.txt", "w")
        for k in range(len(self.lista_pratos)):
            arquivo2.write(str(self.lista_pratos[k].nome_do_prato)) + " "
            arquivo2.write(str(self.lista_pratos[k].valor_do_prato)) + "/n"

        arquivo2.close()

    def salvar_pedido(self):
        arquivo3 = open("lista_pedidos.txt", "w")
        for k in range(len(self.lista_pedidos_dia)):
            arquivo3.write(str(self.lista_pedidos_dia[k].quantidade_vendida)) + " "
            arquivo3.write(str(self.lista_pedidos_dia[k].prato_pedido)) + " "
            arquivo3.write(str(self.lista_pedidos_dia[k].cliente_pediu)) + " "
            arquivo3.write(str(self.lista_pedidos_dia[k].numero_mesa)) + " "
            arquivo3.write(str(self.lista_pedidos_dia[k].disponibilidade_mesa)) + "/n"

        arquivo3.close()

    def salvar_reserva(self):
        arquivo4 = open("lista_reservas.txt", "w")
        for k in range(len(self.lista_nova_reserva)):
            arquivo4.write(str(self.lista_nova_reserva[k].nome_reservou)) + " "
            arquivo4.write(str(self.lista_nova_reserva[k].numero_mesa)) + " "
            arquivo4.write(str(self.lista_nova_reserva[k].data_reservada)) + " "
            arquivo4.write(str(self.lista_nova_reserva[k].hora_reservada)) + "/n"

        arquivo4.close()

    def salvar_funcionario(self):
        arquivo5 = open("lista_funcionarios.txt", "w")
        for k in range(len(self.lista_funcionario)):
            arquivo5.write(str(self.lista_funcionario[k].nome_funcionario)) + " "
            arquivo5.write(str(self.lista_funcionario[k].funcao_exercida)) + " "
            arquivo5.write(str(self.lista_funcionario[k].salario_recebido)) + " "
            arquivo5.write(str(self.lista_funcionario[k].codigo_funcionario)) + " "
            arquivo5.write(str(self.lista_funcionario[k].senha_funcionariio)) + " "
            arquivo5.write(str(self.lista_funcionario[k].email_funcionario)) + "/n"

        arqivo5.close()

    def salvar_login(self):
        arquivo6 = open("lista_login.txt", "w")
        for k in range(len(self.lista_login)):
            arquivo6.write(str(self.lista_login[k].senhaFuncionario)) + " "
            arquivo6.write(str(self.lista_login[k].emailFuncionario)) + "/n"

        arquivo6.close()
 

         
