from Tkinter import *

root = Tk()

photo = PhotoImage(file="3 x 4.JPG")
label = Label(root, image=photo)
label.pack()

root.mainloop()
