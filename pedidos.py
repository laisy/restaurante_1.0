class Pedidos:
    def __init__(self, quantPedida, pratoPedido, clientePedinte):
        self.quantidade_vendida = quantPedida
        self.prato_pedido = pratoPedido
        self.cliente_pediu = clientePedinte

    def __str__(self):
        return "Quantidade pedida: " + str(self.quantidade_vendida) + " | Prato pedido: " +str(self.prato_pedido) + " | Cliente que pediu: " +str(cliente_pediu)
        
