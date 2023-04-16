class Mesa:
    def __init__(self, numeroMesa, disponiblidadeMesa):
        self.numero_mesa = numeroMesa
        self.disponibilidade_mesa = disponiblidadeMesa

    def __str__(self):
        return "Numero da Mesa: " +str(self.numero_mesa)+ " | Disponibilidade: " +str(self.disponibilidade_mesa)



    
