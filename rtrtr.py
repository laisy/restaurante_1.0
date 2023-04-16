from tx import *

cont = Controle()

v = cont.cria_cliente("junior", "23213", "2313")
u = cont.salvar_cliente()

for i in range(len(cont.lista_teste)):
    print cont.lista_teste[i]

