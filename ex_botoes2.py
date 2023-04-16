from Tkinter import *

root = Tk()

def leftClick(event):
    print("Left")
def middleClick(event):
    print("Middle")
def rightClick(event):
    print("Right")

Frame = Frame(root, width=300, height=250)
Frame.bind("<Button-1>", leftClick)
Frame.bind("<Button-2>", middleClick)
Frame.bind("<Button-3>", rightClick)
Frame.pack()

root.mainloop()
