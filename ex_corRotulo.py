from Tkinter import *

root = Tk()

one = Label(root, text="Meu cu", bg="red", fg="white")
one.pack()
two = Label(root, text="Meu pinto", bg="green", fg="black")
two.pack(fill=X)
three = Label(root, text="Meu ovo", bg="blue", fg="white")
three.pack(side=LEFT, fill=Y)
root.mainloop()
