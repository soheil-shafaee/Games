from tkinter import *
import math
import winsound

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#7FE9DE"
TIME = 5
timer_count = NONE
FINISH = 0

# ----------- Content Sections ---------------
window = Tk()
window.config(padx=50, pady=35)
window.iconbitmap("images/images.ico")
window.configure(bg=BACKGROUND_COLOR)
window.title(string="Spy")
window.geometry("700x500")
timer_label = Label(text="Timer",
                    font=("Segoe UI Black", 68, "bold"),
                    fg=FONT_COLOR,
                    bg=BACKGROUND_COLOR)
timer_label.place(x=180, y=30)

# ---------- Timer ----------------
minute = StringVar()
Entry(window,
      textvariable=minute,
      width=2,
      font=("Segoe UI Black", 72, "bold"),
      fg=FONT_COLOR,
      bg=BACKGROUND_COLOR,
      bd=0).place(x=160, y=140)
minute.set("00")

second = StringVar()
Entry(window,
      textvariable=second,
      width=2,
      font=("Segoe UI Black", 72, "bold"),
      fg=FONT_COLOR,
      bg=BACKGROUND_COLOR,
      bd=0).place(x=350, y=140)
second.set("00")

Label(text="min", font=("Segoe UI Black", 12), fg=FONT_COLOR, bg=BACKGROUND_COLOR).place(x=285, y=235)
Label(text="sec", font=("Segoe UI Black", 12), fg=FONT_COLOR, bg=BACKGROUND_COLOR).place(x=475, y=235)


def five_minute():
    minute.set("05")
    second.set("00")


def eight_minute():
    minute.set("08")
    second.set("00")


def ten_minute():
    minute.set("10")
    second.set("00")


start_button = Button(text="Start", bg=FONT_COLOR, bd=0, font=("Segoe UI Black", 10, "bold"), width=20, height=2)
start_button.place(x=245, y=400)

image1 = PhotoImage(file="images/5min.png")
button1 = Button(window, image=image1, bd=0, bg=BACKGROUND_COLOR, command=five_minute)
button1.place(x=150, y=260)

image2 = PhotoImage(file="images/8min.png")
button2 = Button(window, image=image2, bd=0, bg=BACKGROUND_COLOR, command=eight_minute)
button2.place(x=260, y=260)

image3 = PhotoImage(file="images/10min.png")
button3 = Button(window, image=image3, bd=0, bg=BACKGROUND_COLOR, command=ten_minute)
button3.place(x=370, y=260)

window.mainloop()
