from tkinter import *
from game_ui import Background
from tkinter import messagebox

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#7FE9DE"


def is_four():
    messagebox.askokcancel(title="Spy is one", message="When you choose 4 player, you have only one Spy.")


def is_six():
    var = IntVar()

    spy1 = Radiobutton(text="4",
                       variable=var,
                       value=1)
    spy1.place(x=20, y=20)
    spy2 = Radiobutton(text="4",
                       variable=var,
                       value=2)
    spy2.place(x=20, y=50)


class Detail(Background):
    def __init__(self):
        super().__init__()
        self.remove = is_six
        self.window = self.window
        self.var = IntVar()
        # --------- Player Number --------------
        self.player_label = Label(text="Number of Player:",
                                  bg=BACKGROUND_COLOR,
                                  fg=FONT_COLOR,
                                  font=("Segoe UI Black", 28, "bold"))
        self.player_label.place(x=20, y=50)
        self.player_button1 = Radiobutton(text="4",
                                          variable=self.var,
                                          value=1,
                                          bg=BACKGROUND_COLOR,
                                          fg=FONT_COLOR,
                                          font=("Segoe UI Black", 18, "bold"), command=is_four)
        self.player_button1.place(x=450, y=60)
        self.player_button2 = Radiobutton(text="6",
                                          variable=self.var,
                                          value=2,
                                          bg=BACKGROUND_COLOR,
                                          fg=FONT_COLOR,
                                          font=("Segoe UI Black", 18, "bold"),
                                          command=is_six)
        self.player_button2.place(x=450, y=100)
        self.player_button3 = Radiobutton(text="8",
                                          variable=self.var,
                                          value=3,
                                          bg=BACKGROUND_COLOR,
                                          fg=FONT_COLOR,
                                          font=("Segoe UI Black", 18, "bold"))
        self.player_button3.place(x=450, y=140)
        self.submit = Button(text="Play Game", bg=FONT_COLOR, width=20)
        self.submit.place(x=110, y=260)
        self.refresh = Button(text="Remove Info", bg=FONT_COLOR, width=20)
        self.refresh.place(x=110, y=300)
        self.window.mainloop()


Detail()

