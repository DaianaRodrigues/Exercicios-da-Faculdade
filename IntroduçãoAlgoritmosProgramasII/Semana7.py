from tkinter import Tk, Label, PhotoImage, BOTTOM, TOP

root = Tk()
photo = PhotoImage(file='homer.gif').subsample(5)
image = Label(master=root, image=photo)
image.pack(side=TOP)
text = Label(master=root, font=("Courier", 18), text='Olá Mundo!')
text.pack(side=BOTTOM)
root.mainloop()