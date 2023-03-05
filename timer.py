from tkinter import *
import time
import math
import winsound


BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#7FE9DE"
TIMER_COUNT = NONE
DELAY = 0
OLD_DELAY = 50


class Timer:
    def __init__(self):
        # ----------- Background Sections ---------------
        self.window = Tk()
        self.window.config(padx=50, pady=35)
        self.window.iconbitmap("images/images.ico")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.title(string="Spy")
        self.window.geometry("700x550")
        self.timer_label = Label(text="Timer",
                                 font=("Segoe UI Black", 68, "bold"),
                                 fg=FONT_COLOR,
                                 bg=BACKGROUND_COLOR)
        self.timer_label.place(x=180, y=30)

        # ---------- Timer UI ----------------
        self.minute = StringVar()
        self.minute_entry = Entry(self.window,
                                  textvariable=self.minute,
                                  width=2,
                                  font=("Segoe UI Black", 72, "bold"),
                                  fg=FONT_COLOR,
                                  bg=BACKGROUND_COLOR,
                                  bd=0)
        self.minute_entry.place(x=160, y=140)
        self.minute.set("00")

        self.second = StringVar()
        self.second_entry = Entry(self.window,
                                  textvariable=self.second,
                                  width=2,
                                  font=("Segoe UI Black", 72, "bold"),
                                  fg=FONT_COLOR,
                                  bg=BACKGROUND_COLOR,
                                  bd=0)
        self.second_entry.place(x=350, y=140)
        self.second.set("00")

        Label(text="min", font=("Segoe UI Black", 12), fg=FONT_COLOR, bg=BACKGROUND_COLOR).place(x=285, y=235)
        Label(text="sec", font=("Segoe UI Black", 12), fg=FONT_COLOR, bg=BACKGROUND_COLOR).place(x=475, y=235)

        # -------------- Button Image ----------------------
        self.image_play_again = PhotoImage(file="images/play_again.png")
        self.image_menu = PhotoImage(file="images/menu.png")

        # -------------- Suggest Time Image ----------------
        self.image1 = PhotoImage(file="images/5min.png")
        self.button1 = Button(image=self.image1, bd=0, bg=BACKGROUND_COLOR, command=self.five_minute)
        self.button1.place(x=150, y=260)

        self.image2 = PhotoImage(file="images/8min.png")
        self.button2 = Button(image=self.image2, bd=0, bg=BACKGROUND_COLOR, command=self.eight_minute)
        self.button2.place(x=260, y=260)

        self.image3 = PhotoImage(file="images/10min.png")
        self.button3 = Button(image=self.image3, bd=0, bg=BACKGROUND_COLOR, command=self.ten_minute)
        self.button3.place(x=370, y=260)

        # -------------- Start & Finish Button ---------------------
        self.start_button = Button(text="Start",
                                   bg=FONT_COLOR,
                                   bd=0,
                                   font=("Segoe UI Black", 10, "bold"),
                                   width=10,
                                   height=2,
                                   command=self.start_timer,
                                   state=DISABLED)
        self.start_button.place(x=220, y=400)

        self.finish_button = Button(text="Finish",
                                    bg=FONT_COLOR,
                                    bd=0,
                                    font=("Segoe UI Black", 10, "bold"),
                                    width=10,
                                    height=2,
                                    command=self.finish_game)
        self.finish_button.place(x=350, y=400)

        self.window.mainloop()

    # ---------------- Suggest Time ---------------------
    def five_minute(self):
        self.start_button.config(state=NORMAL)
        self.minute.set("05")
        self.second.set("00")

    def eight_minute(self):
        self.start_button.config(state=NORMAL)
        self.minute.set("08")
        self.second.set("00")

    def ten_minute(self):
        self.start_button.config(state=NORMAL)
        self.minute.set("10")
        self.second.set("00")

    # --------------- Timer process --------------------
    def start_timer(self):
        time_change = int(self.minute_entry.get()) * 60
        self.count_down(time_change)

    def count_down(self, mint):
        global TIMER_COUNT
        try:
            self.start_button.configure(state=DISABLED)
            self.button1.configure(state=DISABLED)
            self.button2.configure(state=DISABLED)
            self.button3.configure(state=DISABLED)
        except :
            TIMER_COUNT = NONE

        second_counter = mint % 60
        minute_counter = math.floor(mint / 60)

        if second_counter < 10:
            second_counter = f"0{second_counter}"

        if minute_counter < 10:
            self.minute.set(f"0{minute_counter}")

        else:
            self.minute.set(str(minute_counter))

        self.second.set(second_counter)

        if mint > 0:
            TIMER_COUNT = self.window.after(1000, self.count_down, mint - 1)

        if self.minute.get() == "00" and self.second.get() == "00":
            winsound.PlaySound("mixkit-fairy-message-notification-861.wav", winsound.SND_ASYNC)
            self.finish_game()

    # -------------- Result Display --------------------
    def yes(self):
        global DELAY, OLD_DELAY
        for display_detail in self.window.winfo_children():
            display_detail.destroy()

        canvas = Canvas(self.window, background=BACKGROUND_COLOR, highlightthickness=0)
        winner_canvas = canvas.create_text(180, 100, font=("Segoe UI Black", 32, "bold"))
        canvas.place(x=150, y=50)
        winner_text = "Congratulation\nPeople win.😁"

        for i in range(len(winner_text) + 1):
            word = winner_text[:i]
            print_winner_text = lambda main_word=word: canvas.itemconfig(winner_canvas,
                                                                         text=main_word,
                                                                         fill=FONT_COLOR)
            canvas.after(DELAY, print_winner_text)

            DELAY += OLD_DELAY
            if i > 26:
                play_again = Button(bg=BACKGROUND_COLOR, bd=0, image=self.image_play_again)
                play_again.place(x=210, y=300)
                menu = Button(bg=BACKGROUND_COLOR, bd=0, image=self.image_menu)
                menu.place(x=360, y=300)

    def no(self):
        global DELAY, OLD_DELAY
        for display_detail in self.window.winfo_children():
            display_detail.destroy()
        canvas = Canvas(self.window, background=BACKGROUND_COLOR, highlightthickness=0)
        spy_canvas = canvas.create_text(180, 100, font=("Segoe UI Black", 32, "bold"))
        canvas.place(x=150, y=50)
        spy_text = "The Winner is \n       spy 😈!!"
        for i in range(len(spy_text) + 1):
            word = spy_text[:i]
            print_text = lambda main_word=word: canvas.itemconfig(spy_canvas, text=main_word, fill=FONT_COLOR)
            canvas.after(DELAY, print_text)
            DELAY += OLD_DELAY
            if i > 26:
                play_again = Button(bg=BACKGROUND_COLOR, bd=0, image=self.image_play_again)
                play_again.place(x=210, y=300)
                menu = Button(bg=BACKGROUND_COLOR, bd=0, image=self.image_menu)
                menu.place(x=360, y=300)

        winsound.PlaySound("SF-laughter2.wav", winsound.SND_ASYNC)

    def finish_game(self):
        time.sleep(1)
        for details in self.window.winfo_children():
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
                            height=2,
                            command=self.yes)
        yes_button.place(x=200, y=200)

        no_button = Button(text="NO",
                           bg=FONT_COLOR,
                           bd=0,
                           font=("Segoe UI Black", 10, "bold"),
                           width=10,
                           height=2,
                           command=self.no)
        no_button.place(x=350, y=200)

