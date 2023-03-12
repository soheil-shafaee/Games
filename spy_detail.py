import random
from tkinter import *
from spy import Spy
from timer import Timer

BACKGROUND_COLOR = "#434242"
FONT_COLOR = "#7FE9DE"

words = ['a', 'b', 'c', 'd']


class Detail(Spy):
    def __init__(self):
        self.window = Tk()
        self.window.config(padx=50, pady=35)
        self.window.iconbitmap("images/images.ico")
        self.window.configure(bg=BACKGROUND_COLOR)
        self.window.title(string="Spy")
        self.window.geometry("700x550")
        self.players_list = []
        self.players_intvar = IntVar()
        self.spies_intvar = IntVar()
        self.players_intvar.set(4)
        self.spies_intvar.set(1)
        self.players_quantity = self.players_intvar.get()
        self.spies = self.spies_intvar.get()
        self.peoples = self.players_quantity - self.spies
        self.word = random.choice(words)
        self.character_label = Label(text="",
                                     bg=BACKGROUND_COLOR,
                                     fg=FONT_COLOR,
                                     font=("Segoe UI Black", 28, "bold"))
        # --------- Images Section -------------
        self.player_ch = PhotoImage(file="images/player character.png")
        self.reset_info = PhotoImage(file="images/Reset_inf.png")
        self.let_start = PhotoImage(file="images/let_go.png")
        # --------- Player Number --------------
        self.player_label = Label(text="Number of Player:",
                                  bg=BACKGROUND_COLOR,
                                  fg=FONT_COLOR,
                                  font=("Segoe UI Black", 28, "bold"))
        self.player_label.place(x=20, y=50)

        self.player_button1 = Radiobutton(text="4",
                                          variable=self.players_intvar,
                                          value=4,
                                          bg=BACKGROUND_COLOR,
                                          fg=FONT_COLOR,
                                          font=("Segoe UI Black", 18, "bold"),
                                          command=self.players_num)
        self.player_button1.place(x=450, y=60)

        self.player_button2 = Radiobutton(text="6",
                                          variable=self.players_intvar,
                                          value=6,
                                          bg=BACKGROUND_COLOR,
                                          fg=FONT_COLOR,
                                          font=("Segoe UI Black", 18, "bold"),
                                          command=self.players_num
                                          )
        self.player_button2.place(x=450, y=100)

        self.player_button3 = Radiobutton(text="8",
                                          variable=self.players_intvar,
                                          value=8,
                                          bg=BACKGROUND_COLOR,
                                          fg=FONT_COLOR,
                                          font=("Segoe UI Black", 18, "bold"),
                                          command=self.players_num
                                          )
        self.player_button3.place(x=450, y=140)

        self.spy1 = Radiobutton(text="1",
                                variable=self.spies_intvar,
                                value=1,
                                bg=BACKGROUND_COLOR,
                                fg=FONT_COLOR,
                                font=("Segoe UI Black", 18, "bold"),
                                command=self.players_num
                                )

        self.spy2 = Radiobutton(text="2",
                                variable=self.spies_intvar,
                                value=2,
                                bg=BACKGROUND_COLOR,
                                fg=FONT_COLOR,
                                font=("Segoe UI Black", 18, "bold"),
                                command=self.players_num
                                )
        self.spy3 = Radiobutton(text="3",
                                variable=self.spies_intvar,
                                value=3,
                                bg=BACKGROUND_COLOR,
                                fg=FONT_COLOR,
                                font=("Segoe UI Black", 18, "bold"),
                                command=self.players_num
                                )
        self.submit = Button(image=self.player_ch,
                             bg=FONT_COLOR,
                             borderwidth=0,
                             compound=CENTER,
                             command=self.players_num
                             )
        self.submit.place(x=110, y=230)
        self.start_button = Button(image=self.let_start,
                                   bg=FONT_COLOR,
                                   borderwidth=0,
                                   compound=CENTER,
                                   command=self.spy_game
                                   )
        self.refresh = Button(image=self.reset_info,
                              bg=FONT_COLOR,
                              borderwidth=0,
                              compound=CENTER,
                              command=self.edit
                              )
        self.refresh.place(x=110, y=300)
        self.window.mainloop()

    def is_6(self):
        self.player_label.config(text="How many Spy? ")
        self.submit.config(state=DISABLED)
        self.player_button1.config(state=DISABLED)
        self.player_button2.config(state=DISABLED)
        self.player_button3.config(state=DISABLED)
        self.spy1.place(x=450, y=220)
        self.spy2.place(x=450, y=260)
        self.spy3.place(x=450, y=300)
        self.players_quantity = self.players_intvar.get()
        self.spies = self.spies_intvar.get()
        if self.spies_intvar.get():
            self.start_button.place(x=80, y=370)

    def players_num(self):
        if self.players_intvar.get() == 4:
            self.start_button.place(x=80, y=370)
            self.players_quantity = 4
            self.spies = 1
        elif self.players_intvar.get() == 6 or 8:
            self.spies = self.spies_intvar.get()
            self.submit.config(command=self.is_6)

    def spies_num(self):
        self.spies = self.spies_intvar.get()

    def start_game_button(self):
        print(f'Players: {self.players_quantity}\n'
              f'people: {int(self.players_quantity - self.spies)}\n'
              f'spy: {self.spies}\n{self.word}')
        self.player_button1.config(state=DISABLED)
        self.player_button2.config(state=DISABLED)
        self.player_button3.config(state=DISABLED)
        self.spy1.config(state=DISABLED)
        self.spy2.config(state=DISABLED)
        self.spy3.config(state=DISABLED)
        self.submit.config(state=DISABLED)

    def edit(self):
        self.window.destroy()
        Detail()

    def remove_label(self):
        self.character_label.place_forget()

    def spy_logic(self):
        self.character_label = Label(text="",
                                     bg=BACKGROUND_COLOR,
                                     fg=FONT_COLOR,
                                     font=("Segoe UI Black", 28, "bold"))
        self.character_label.place(x=20, y=50)
        next_button = Button(text="Next_player", bg=FONT_COLOR, width=30, command=self.remove_label)
        character = random.choice(self.players_list)

        if character == 'People':
            self.character_label.config(text=f'You are a people!\nThe word is {self.word}')
            next_button.place(x=110, y=300)

        else:
            self.character_label.config(text='You are a Spy!')
            next_button.place(x=110, y=300)
        self.players_list.remove(character)
        print(self.players_list)
        if len(self.players_list) == 0:
            self.window.destroy()
            Timer()

    def spy_game(self):
        self.peoples = self.players_quantity - self.spies
        for people in range(self.peoples):
            self.players_list.append('People')
        for spy in range(self.spies):
            self.players_list.append('Spy')
        print(f'Players: {self.players_quantity}\n'
              f'people: {int(self.players_quantity - self.spies)}\n'
              f'spy: {self.spies}\n{self.word}\n'
              f'All Players: {len(self.players_list)}\n'
              f'List: {self.players_list}')
        for data in self.window.winfo_children():
            data.destroy()

        self.start_button = Button(text="Next", bg=FONT_COLOR, width=30, command=self.spy_logic)
        self.start_button.place(x=150, y=260)


def play_game():
    Detail()

