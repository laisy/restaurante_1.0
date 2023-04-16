class Cliente:
    def __init__(self, nomeCliente, dataVisita, idCliente):
        self.novo_cliente = nomeCliente
        self.nova_visita = dataVisita
        self.novo_id = idCliente


    def __str__(self):
        return "Nome do cliente: " + str(self.novo_cliente) + " | Data Visita: " +str(self.nova_visita) + " | Id Cliente: " +str(self.novo_id)
