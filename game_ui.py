from tkinter import *

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#F3EFE0"

# --------- Content Section ----------------
window = Tk()
window.config(padx=50, pady=35)
window.iconbitmap("images/images.ico")
window.configure(bg=BACKGROUND_COLOR)
window.title(string="Spy")
window.geometry("700x500")


# -------- Text Section  ------------
text = Label(text="Who's Spy ?",
             font=("Segoe UI Black", 17, "bold"),
             bg=BACKGROUND_COLOR,
             fg=FONT_COLOR)
text.place(x=300, y=5, anchor="center")

# -------- Image Section ------------
canvas = Canvas(width=300, height=360, bg=BACKGROUND_COLOR, highlightthickness=0)
spy_image = PhotoImage(file="images/spy.png")
play_image = PhotoImage(file="images/play.png")
menu_image = PhotoImage(file="images/menu1.png")
canvas.create_image(180, 180, image=spy_image)
canvas.place(x=125, y=25)

# ---------- Button Section  -----------
play_button = Button(text="Play Game",
                     image=play_image,
                     borderwidth=0,
                     bg=BACKGROUND_COLOR)
play_button.place(x=200, y=390)
menu_button = Button(text="Menu",
                     image=menu_image,
                     borderwidth=0,
                     bg=BACKGROUND_COLOR)
menu_button.place(x=350, y=390)

# ---------- Display Section -----------
window.mainloop()
