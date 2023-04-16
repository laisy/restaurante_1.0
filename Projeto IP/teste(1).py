from mesa import *
from cliente import *
from prato import *
from pedido import *

class Controlador:
    def __init__(self):
        self.lista_cliente = []
        arquivo = open("", "r")
        
        

        
        self.lista_funcionario = []
        self.lista_login = []
        self.lista_pratos = []
        self.lista_pedidos_dia = []
        self.lista_lucro = []
        self.lista_nova_reserva = []

    def cadastra_cliente(nomeCliente, dataVisita, dataReserva):
        novo_cliente = Cliente(nomeCliente, dataVisista, dataReserva)
        self.lista_cliente.append(novo_cliente)

    def cadastra_prato(nomePrato, valorPrato, qtdEstoque):
        novo_prato = Prato(nomePrato, valorPrato, qtdEstoque)
        self.lista_pratos.append(novo_prato)

    def registra_pedido_cliente(quantidadePedida, pratoPedido, nomeCliente, localMesa, disponibiliMesa):
        pedido = Pedido(quantidadePedida, pratoPedido, nomeCliente)
        mesa_pedida = Mesa(localMesa, disponibiliMesa)
        self.lista_pedidos_dia.append(pedido, mesa_pedida)

    def definindo_uma_mesa(self, localMesa, disponibilidadeMesa, nomeCliente, visitaCliente, reservaCliente):
        nova_mesa = Mesa(localMesa, disponibilidadeMesa)
        novo_cliente = Cliente(nomeCliente, visitaCliente, reservaCliente)
        self.lista_nova_reserva.append(nova_mesa, novo_cliente)
    
   def salvar(self):
       arquivo = open("lista_clientes.txt", "w")
       for k in range(len(self.lista_cliente)):
           arquivo.write(str(self.lista_cliente[k].nome)) + " "
           arquivo.write(str(self.lista_cliente[k].cpf)) + "\n"



        
