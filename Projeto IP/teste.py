from mesa import *
from cliente import *
from prato import *
from pedido import *

class Controlador:
    def __init__(self):
        self.lista_cliente = []
        arq1 = open("lista_clientes.txt", "r")
        splitou = arq1.split()
        for i in range(len(splitou)):
            nome = splitou[0]
            dataR = splitou[1]
            identidade = splitou[2]
            self.lista_cliente.append(nome)
            self.lista_cliente.append(dataR)
            self.lista_client.append(identidade)

        arq.close
        
        self.lista_funcionario = []
        arq2 = open("lista_funcionarios.txt", "r")
        splitou = arq2.split()
        for i in range(len(splitou)):
            nome = splitou[0]
            funcao_funcionario = splitou[1]
            salario_funcionario= splitou[2]
            codigo_funcionario = splitou[3]
            senha_funcionario = splitou[4]
            email_funcionario = splitou[5]
            self.lista_funcionario.append(nome)
            self.lista_funcionario.append(funcao_funcionario)
            self.lista_funcionario.append(salario_funcionario)
            self.lista_funcionario.append(codigo_funcionario)
            self.lista_login.append(senha_funcionario)
            self.lista_login.append(email_funcionario)

        arq2.close

        self.lista_login = []

        self.lista_pratos = []
        arq3 = open("lista_pratos.txt", "r")
        splitou = arq3.split()
        for i in range(len(splitou)):
            nome_prato = splitou[0]
            valor_prato = splitou[1]
            self.lista_pratos.append(nome_prato)
            self.lista_pratos.append(valor_prato)
            
        arq3.close

        
        self.lista_pedidos_dia = []
        arq4 = open("lista_pedidos.txt", "r")
        splitou = arq4.split()
        for i in range(len(splitou)):
            quantidade_pedida = splitou[0]
            prato_pedido = splitou[1]
            nome_cliente = splitou[2]
            local_mesa = splitou[3]
            disponibilidade_mesa = splitou[4]
            self.lista_pedidos.append(quantidade_pedida)
            self.lista_pedidos.append(prato_pedido)
            self.lista_pedidos.append(nome_cliente)
            self.lista_pedidos.append(local_mesa)
            self.lista_pedidos.append(disponibilidade_mesa)


        arq4.close

        self.lista_lucro = []
        self.lista_nova_reserva = []

    def cadastra_cliente(nomeCliente, dataVisita, idCliente):
        novo_cliente = Cliente(nomeCliente, dataVisita, idClient)
        self.lista_cliente.append(novo_cliente)

    def cadastra_prato(nomePrato, valorPrato):
        novo_prato = Prato(nomePrato, valorPrato)
        self.lista_pratos.append(novo_prato)

    def registra_pedido_cliente(quantidadePedida, pratoPedido, nomeCliente, localMesa, disponibiliMesa):
        pedido = Pedido(quantidadePedida, pratoPedido, nomeCliente)
        mesa_pedida = Mesa(numeroMesa, disponibilidadeMesa)
        self.lista_pedidos_dia.append(pedido)
        self.lista_pedidos.append(mesa_pedida)

    def definindo_uma_reserva(nomeReservista, numeroMesa, dataReservada, horaReservada):
        nova_reserva = Reserva(nomeReservista, numeroMesa, dataReservada, horaReservada) 
        self.lista_nova_reserva.append(nova_reserva)

    def cadastrando_funcionario(nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario, senhaFuncionario, emailFuncionario):
        novo_funcionario = Funcionario(nomeFuncionario, funcaoFuncionario, salarioFUncionario, codigoFuncionario, senhaFuncionario, emailFuncionario)
        self.lista_funcionarios.append(novo_funcionario)
        
        
    
   def salvar_cliente(self):
       arquivo1 = open("lista_clientes.txt", "w")
       for k in range(len(self.lista_cliente)):
           arquivo1.write(str(self.lista_cliente[k].nomeCliente)) + " "
           arquivo1.write(str(self.lista_cliente[k].dataVisita)) + " "
           arquivo1.write(str(self.lista_cliente[k].idCliente)) + "/n"


       arquivo1.close()

   def salvar_prato(self):
       arquivo2 = open("lista_pratos.txt", "w")
       for k in range(len(self.lista_pratos)):
           arquivo2.write(str(self.lista_cliente[k].nomePrato)) + " "
           arquivo2.write(str(self.lista_cliente[k].valorPrato)) + "/n

       arquivo2.close()

   def salvar_pedido(self):
       arquivo3 = open("lista_pedidos.txt", "w")
       for k in range(len(self.lista_pedidos_dia)):
           arquivo3.write(str(self.lista_cliente[k].pedido)) + " "
           arquivo3.write(str(self.lista_cliente[k].mesa_pedida)) + "/n"

       arquivo3.close()

    def salvar_reserva(self):
       arquivo4 = open("lista_reserva.txt", "w")
       for k in range(len(self.lista_nova_reserva)):
           arquivo4.write(str(self.lista_nova_reserva[k].nomeReservista)) + " "
           arquivo4.write(str(self.lista_nova_reserva[k].numeroMesa)) + " "
           arquivo4.write(str(self.lista_nova_reserva[k].dataReservada)) + " "
           arquivo4.write(str(self.lista_nova_reserva[k].horaReservada)) + "/n"
           
       arquivo4.close()

    def salvar_funcionario(self):
        arquivo5 = open("lista_funcionarios.txt", "w")
        for k in range(len(self.lista_funcionario)):
            arquivo5.write(str(self.lista_funcionario[k].nomeFuncionario)) + " "
            arquivo5.write(str(self.lista_funcionario[k].funcaoFuncionario)) + " "
            arquivo5.write(str(self.lista_funcionario[k].salarioFuncionario)) + " "
            arquivo5.write(str(self.lista_funcionario[k].codigoFuncionario)) + " "
            arquivo5.write(str(self.lista_funcionario[k].senhaFuncionariio)) + " "
            arquivo5.write(str(self.lista_funcionario[k].emailFuncionario)) + "/n"

        arqivo5.close


         
