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
        self.lista_login = []
        self.lista_pratos = []
        self.lista_pedidos_dia = []
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

    def definindo_uma_reserva(self, numeroMesa, disponibilidadeMesa, nomeCliente, visitaCliente, idCliente):
        nova_mesa = Mesa(numeroMesa, disponibilidadeMesa)
        novo_cliente = Cliente(nomeCliente, visitaCliente, idCliente)
        self.lista_nova_reserva.append(nova_mesa)
        self.lista_nova_reserva.append(novo_cliente)
    
   def salvar_cliente(self):
       arquivo = open("lista_clientes.txt", "w")
       for k in range(len(self.lista_cliente)):
           arquivo.write(str(self.lista_cliente[k].nomeCliente)) + " "
           arquivo.write(str(self.lista_cliente[k].dataVisita)) + " "
           arquivo.write(str(self.lista_cliente[k].idCliente)) + "/n"


       arquivo.close()

   def salvar_prato(self):
       arquivo = open("lista_pratos.txt", "w")
       for k in range(len(self.lista_pratos)):
           arquivo.write(str(self.lista_cliente[k].nomePrato)) + " "
           arquivo.write(str(self.lista_cliente[k].valorPrato)) + "/n"

       arquivo.close()

   def salvar_pedido(self):
       arquivo = open("lista_pedidos.txt", "w")
       for k in range(len(self.lista_pedidos_dia)):
           arquivo.write(str(self.lista_cliente[k].pedido)) + " "
           arquivo.write(str(self.lista_cliente[k].mesa_pedida)) + "/n"

       arquivo.close()

    def salvar_reserva(self):
       arquivo = open("lista_reserva.txt", "w")
       for k in range(len(self.lista_nova_reserva)):
           arquivo.write(str(self.lista_cliente[k].nova_mesa)) + " "
           arquivo.write(str(self.lista_cliente[k].novo_cliente)) + "/n"

       arquivo.close()

           

           





        
