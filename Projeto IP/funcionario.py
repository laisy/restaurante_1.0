class Funcionario:
    def __init__(self, nomeFuncionario, funcaoFuncionario, salarioFuncionario, codigoFuncionario, senhaFuncionario, emailFuncionario):
        self.nome_funcionario = nomeFuncionario
        self.funcao_exercida = funcaoFuncionario
        self.salario_recebido = float(salarioFuncionario)
        self.codigo_funcionario = codigoFuncionario
        self.senha_do_login = senhaFuncionario
        self.email_do_login = emailFuncionario

