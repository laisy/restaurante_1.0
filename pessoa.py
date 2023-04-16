from datetime import date

class Pessoa:

    def __init__(self, novo_nome, novo_nascimento, novo_sexo, novo_endereco, nova_cidade, novo_celular, novo_ativo):
        
        self.nome = novo_nome
        self.nascimento = novo_nascimento  
        self.sexo = novo_sexo
        self.endereco = novo_endereco
        self.cidade = nova_cidade
        self.celular = novo_celular
        self.ativo = novo_ativo



    def __init__(self, nome_aluno, nova_nota, novo_idioma, nova_data):
    #Boletim

        self.aluno = novo_aluno
        self.nota = nova_nota
        self.idioma = novo_idioma
        self.data = nova_data


