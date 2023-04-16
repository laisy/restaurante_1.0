from teste import *

cont = Controlador()


x = cont.cadastrando_funcionario("Valdir", "Cozinheiro", "900,00", "000003", "valdirjunior@gmail.com", "amocozinhar12")
y = cont.salvar_funcionario()






for i in range(len(cont.lista_funcionario)):
    print cont.lista_funcionario[i]


