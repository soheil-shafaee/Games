from tkinter import *

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#F3EFE0"


class Background:
    def __init__(self):
        self.window = None
        self.bg()

    def bg(self):
        self.window = Tk()
        self.window.config(padx=50, pady=35)
        self.window.iconbitmap("images/images.ico")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.title(string="Spy")
        self.window.geometry("700x500")

    def main_loop(self):
        self.window.mainloop()


class SpyInterface(Background):

    def __init__(self):
        super().__init__()
        # --------- Background Section ----------------
        self.window = self.window
        # -------- Text Section  ------------
        self.text = Label(text="Who's Spy ?",
                          font=("Segoe UI Black", 17, "bold"),
                          bg=BACKGROUND_COLOR,
                          fg=FONT_COLOR)
        self.text.place(x=300, y=5, anchor="center")

        # -------- Image Section ------------
        self.canvas = Canvas(width=300, height=360, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.spy_image = PhotoImage(file="images/spy.png")
        self.play_image = PhotoImage(file="images/play.png")
        self.menu_image = PhotoImage(file="images/menu1.png")
        self.canvas.create_image(180, 180, image=self.spy_image)
        self.canvas.place(x=125, y=25)

        # ---------- Button Section  -----------
        self.play_button = Button(text="Play Game",
                                  image=self.play_image,
                                  bd=0,
                                  bg=BACKGROUND_COLOR)
        self.play_button.place(x=200, y=390)
        self.menu_button = Button(text="Menu",
                                  image=self.menu_image,
                                  borderwidth=0,
                                  bg=BACKGROUND_COLOR)
        self.menu_button.place(x=350, y=390)

        # ---------- Display Section -----------
        self.window.mainloop()


