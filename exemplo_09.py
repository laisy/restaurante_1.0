from Tkinter import *
from tkMessageBox import *


root = Tk()

showinfo('Alerta','Vamos coma�ar uma sequ�ncia de perguntas')

answer = askquestion('Pergunta','Voc� conhece Tony Montana?')

if answer == 'yes':
    showerror('Cuidado','Afaste-se dele!')
else:
    showwarning('O Grande Irm�o zela por ti','Tudo bem. Mas ficaremos de olho em voc�')


root.mainloop()
