from Tkinter import *

root = Tk()

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

button1 = Button(topFrame, text="Meu cu", fg="purple")
button2 = Button(topFrame, text="Meu pinto", fg="red")
button3 = Button(bottomFrame, text="Meu ovo", fg="blue")
button1.pack(side=LEFT)
button2.pack(side=LEFT)
button3.pack(side=BOTTOM)

root.mainloop()
