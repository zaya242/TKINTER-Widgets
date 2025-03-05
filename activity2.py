from tkinter import *
from tkinter import messagebox

window=Tk()

window.title=("TKinter message box")

def msg():
    messagebox.showwarning("Danger!,Virus Detected")

label=Label(master=window,text="Messagebox in Tkinter")
button=Button(master=window,text="Click Here!",command=msg)

label.pack()
button.pack()

window.mainloop()