from Tkinter import *

root = Tk()

def printName():
    print ("Bem na sua cara!")

button_1 = Button(root, text="Eu vou rebolar", command=printName)
button_1.pack()

root.mainloop()
