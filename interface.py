from Tkinter import *

def FazerVariosNada():
    print("Nada ainda...")

root = Tk()
root.geometry("600x400")
root.title("Turismo Ecologico")

menu =  Menu(root)
root.config(menu=menu)

subMenu = Menu(menu)
menu.add_cascade(label="Cadastros", menu=subMenu)
subMenu.add_command(label="Novo cliente", command=FazerVariosNada)
subMenu.add_command(label="Novo pacote", command=FazerVariosNada)
subMenu.add_separator()
subMenu.add_command(label="Sair", command=FazerVariosNada)

editMenu = Menu(menu)
menu.add_cascade(label="Vendas", menu=editMenu)
editMenu.add_command(label="Pacotes", command=FazerVariosNada)

# ***** Toolbar *****

toolbar = Frame(root, bg="blue")
insertButt = Button(toolbar, text="Entrar", command=FazerVariosNada)
insertButt.pack(side=LEFT, padx=2, pady=2)
printButt= Button(toolbar, text="Pacotes disponiveis", command=FazerVariosNada)
printButt.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** ABAS *****

status = Label(root, text="Eu vou rebolar bem na sua cara!", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
