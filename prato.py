class Prato:
    def __init__(self, nomePrato, valorPrato):
        self.nome_do_prato = nomePrato
        self.valor_do_prato = valorPrato

    def __str__(self):
        return "Nome do Prato: " + str(self.nome_do_prato) + " | Valor do Prato: " + str(self.valor_do_prato)


