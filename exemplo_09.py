from Tkinter import *
from tkMessageBox import *


root = Tk()

showinfo('Alerta','Vamos comaçar uma sequência de perguntas')

answer = askquestion('Pergunta','Você conhece Tony Montana?')

if answer == 'yes':
    showerror('Cuidado','Afaste-se dele!')
else:
    showwarning('O Grande Irmão zela por ti','Tudo bem. Mas ficaremos de olho em você')


root.mainloop()
