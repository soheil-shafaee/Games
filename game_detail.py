from tkinter import *

root = Tk()
var = IntVar()

root.geometry("700x500")

player_label = Label(text="Number of Player:")
player_label.place(x=20, y=10)

player_button1 = Radiobutton(root, text="4", variable=var, value=1)
player_button1.place(x=150, y=10)

player_button2 = Radiobutton(root, text="6", variable=var, value=2)
player_button2.place(x=150, y=30)

player_button3 = Radiobutton(root, text="8", variable=var, value=3)
player_button3.place(x=150, y=50)

submit = Button(text="Submit", )

root.mainloop()
