class Funcionario:
    def __init__(self, nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario, emailFuncionario, senhaFuncionario):
        self.nome_funcionario = nomeFuncionario
        self.funcao_exercida = funcaoFuncionario
        self.salario_recebido = salarioFuncionario
        self.codigo_funcionario = codigoFuncionario
        self.email_funcionario = emailFuncionario
        self.senha_funcionario = senhaFuncionario

    def __str__(self):
        return "Nome do funcionario: " +str(self.nome_funcionario) + " | Funcao Exercida: " +str(self.funcao_exercida) + "Salario Recebido: " +str(self.salario_recebido) + " | Codigo Funcionario: " +str(self.codigo_funcionario) + " | Email: " + str(self.email_funcionario) + " | Senha: " + str(self.senha_funcionario)

