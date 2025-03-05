from tkinter import *
from PIL import Image, ImageTk

window=Tk()
window.title("TKinter image")

upload=Image.open("img1.jpg")
upload=Image.open("img2.jpg")

image=ImageTk.PhotoImage(upload)

label=Label(master=window,image=image)
label1=Label(master=window,text="Thia is how to add an image")

label.pack()
label1.pack()

window.mainloop()
