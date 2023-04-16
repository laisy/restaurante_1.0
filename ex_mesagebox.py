from Tkinter import *
import Tkinter.messagebox

root = Tk()

Tkinter.messagebox.showinfo("Window Title", "Monkeys can live at 300 years.")

answer = Tkinter.messagebox.askquestion("Question 1", "Do you like cocks?")
if answer == "yes":
    print("8====D")

root.mainloop()
