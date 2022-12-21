from tkinter import *
import math
import winsound

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#7FE9DE"
TIME = 5
timer_count = NONE
FINISH = 0


# ----------- Content Sections ---------------
class Timer:
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=50, pady=35)
        self.window.iconbitmap("images/images.ico")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.title(string="Spy")
        self.window.geometry("700x500")
        self.canvas = Canvas(width=800, height=500, bg=BACKGROUND_COLOR, highlightthickness=0)

        self.text = Label(self.canvas, text="Timer", font=("Segoe UI Black", 72, "bold"), fg=FONT_COLOR,
                          bg=BACKGROUND_COLOR)
        self.text.place(x=155, y=-35)

        self.timer = self.canvas.create_text(310,
                                             130,
                                             text="00:00",
                                             font=("Segoe UI Black", 72, "bold"),
                                             fill=FONT_COLOR)
        self.canvas.place(x=10, y=80)

        self.start_button = Button(text="Start", width=10, bg=FONT_COLOR, command=self.start_time)
        self.start_button.place(x=180, y=300)

        self.stop_button = Button(text="Stop", width=10, bg=FONT_COLOR, command=self.restart_time)
        self.stop_button.place(x=400, y=300)

        self.window.mainloop()

    # ---------- Timer Process ------------------
    def start_time(self):
        work_sec = TIME * 60
        self.start_button.config(state=DISABLED)
        self.count_down(work_sec)

    def restart_time(self):
        self.window.after_cancel(timer_count)
        self.start_button.config(state=NORMAL)
        self.canvas.itemconfig(self.timer, text="00:00")

    def count_down(self, time):
        second = time % 60
        minute = math.floor(time / 60)
        if second < 10:
            second = f"0{second}"
            if minute == 0 and second == f"0{0}":
                global FINISH
                FINISH += 1
                if FINISH % 1 == 0:
                    winsound.PlaySound("mixkit-fairy-message-notification-861.wav", winsound.SND_ASYNC)
        self.canvas.itemconfig(self.timer, text=f"{minute}:{second}")
        if time > 0:
            global timer_count
            timer_count = self.window.after(1000, self.count_down, time - 1)


Timer()
