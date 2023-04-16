class Login:
    def __init__(self, emailFuncionario, senhaFuncionario):
        self.email_funcionario = emailFuncionario
        self.senha_funcionario = senhaFuncionario

    def __str__(self):
        return "Email do funcionario: " +str(self.email_funcionario) + " | Senha do Funcionario: " +str(self.senha_funcionario)
