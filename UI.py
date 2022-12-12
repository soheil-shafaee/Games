from tkinter import *

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#F3EFE0"
# --------- Content Section ----------------
window = Tk()
window.config(padx=20, pady=20)
window.iconbitmap("images/images.ico")
window.configure(bg=BACKGROUND_COLOR)
window.title(string="Spy")
window.geometry("700x500")
# -------- Text Section  ------------
text = Label(text="Who's Spy?", font=("Times new roman", 17, "bold"), bg=BACKGROUND_COLOR, fg=FONT_COLOR)
text.grid(row=0, column=1)
# -------- Image Section ------------
canvas = Canvas(width=400, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
spy_image = PhotoImage(file="images/spy.png")
play_image = PhotoImage(file="images/play.png")
menu_image = PhotoImage(file="images/menu1.png")
canvas.create_image(200, 300, image=spy_image)
canvas.grid(row=1, column=1)

# ---------- Button Section  -----------
play_button = Button(window,
                     text="Play Game",
                     image=play_image,
                     borderwidth=0,
                     bg=BACKGROUND_COLOR)
play_button.grid(row=2, column=1)
menu_button = Button(text="Menu",
                     image= menu_image,
                     borderwidth=0,
                     bg=BACKGROUND_COLOR)
menu_button.grid(row=2, column=2)
# ---------- Display Section -----------
window.mainloop()
