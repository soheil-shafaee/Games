from tkinter import *
import time
import math
import winsound

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#7FE9DE"
timer_count = NONE

# ----------- Background Sections ---------------
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

# ---------- Timer UI ----------------
minute = StringVar()
minute_entry = Entry(window,
                     textvariable=minute,
                     width=2,
                     font=("Segoe UI Black", 72, "bold"),
                     fg=FONT_COLOR,
                     bg=BACKGROUND_COLOR,
                     bd=0)
minute_entry.place(x=160, y=140)
minute.set("00")

second = StringVar()
second_entry = Entry(window,
                     textvariable=second,
                     width=2,
                     font=("Segoe UI Black", 72, "bold"),
                     fg=FONT_COLOR,
                     bg=BACKGROUND_COLOR,
                     bd=0)
second_entry.place(x=350, y=140)
second.set("00")

Label(text="min", font=("Segoe UI Black", 12), fg=FONT_COLOR, bg=BACKGROUND_COLOR).place(x=285, y=235)
Label(text="sec", font=("Segoe UI Black", 12), fg=FONT_COLOR, bg=BACKGROUND_COLOR).place(x=475, y=235)


# ---------------- Suggest Time ---------------------
def five_minute():
    start_button.config(state=NORMAL)
    minute.set("05")
    second.set("00")


def eight_minute():
    start_button.config(state=NORMAL)
    minute.set("08")
    second.set("00")


def ten_minute():
    start_button.config(state=NORMAL)
    minute.set("10")
    second.set("00")


# --------------- Timer process --------------------
def start_timer():
    time_change = int(minute_entry.get()) * 60
    count_down(time_change)


def count_down(mint):
    start_button.config(state=DISABLED)
    button1.config(state=DISABLED)
    button2.config(state=DISABLED)
    button3.config(state=DISABLED)
    second_counter = mint % 60
    minute_counter = math.floor(mint / 60)
    if second_counter < 10:
        second_counter = f"0{second_counter}"
    if minute_counter < 10:
        minute.set(f"0{minute_counter}")
    else:
        minute.set(str(minute_counter))
    second.set(second_counter)
    if mint > 0:
        global timer_count
        timer_count = window.after(1000, count_down, mint - 1)

    if minute.get() == "00" and second.get() == "00":
        winsound.PlaySound("mixkit-fairy-message-notification-861.wav", winsound.SND_ASYNC)


# -------------- Result Display --------------------
def yes():
    for display_detail in window.winfo_children():
        display_detail.destroy()


def no():
    for display_detail in window.winfo_children():
        display_detail.destroy()
    mafia_image = PhotoImage(file="images/mafia.jpg")
    canvas = Canvas(width=1600, height=1200, bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.create_image(300, 310, image=mafia_image)
    canvas.place(x=100, y=100)


def finish_game():
    time.sleep(1)
    for details in window.winfo_children():
        details.destroy()
    Label(text="Do you find spy?",
          font=("Segoe UI Black", 25, "bold"),
          fg=FONT_COLOR,
          bg=BACKGROUND_COLOR).place(x=180, y=50)
    yes_button = Button(text="YES",
                        bg=FONT_COLOR,
                        bd=0,
                        font=("Segoe UI Black", 10, "bold"),
                        width=10,
                        height=2)
    yes_button.place(x=200, y=200)

    no_button = Button(text="NO",
                       bg=FONT_COLOR,
                       bd=0,
                       font=("Segoe UI Black", 10, "bold"),
                       width=10,
                       height=2,
                       command=no)
    no_button.place(x=350, y=200)


# -------------- Suggest Time Image ----------------
image1 = PhotoImage(file="images/5min.png")
button1 = Button(window, image=image1, bd=0, bg=BACKGROUND_COLOR, command=five_minute)
button1.place(x=150, y=260)

image2 = PhotoImage(file="images/8min.png")
button2 = Button(window, image=image2, bd=0, bg=BACKGROUND_COLOR, command=eight_minute)
button2.place(x=260, y=260)

image3 = PhotoImage(file="images/10min.png")
button3 = Button(window, image=image3, bd=0, bg=BACKGROUND_COLOR, command=ten_minute)
button3.place(x=370, y=260)

# -------------- Start & Finish Button ---------------------
start_button = Button(text="Start",
                      bg=FONT_COLOR,
                      bd=0,
                      font=("Segoe UI Black", 10, "bold"),
                      width=10,
                      height=2,
                      command=start_timer,
                      state=DISABLED)
start_button.place(x=220, y=400)

finish_button = Button(text="Finish",
                       bg=FONT_COLOR,
                       bd=0,
                       font=("Segoe UI Black", 10, "bold"),
                       width=10,
                       height=2,
                       command=finish_game)
finish_button.place(x=350, y=400)
window.mainloop()
