# Import the required libraries
from tkinter import *
from spy import Spy

words = ['a', 'b', 'c', 'd']
# Create an instance of tkinter frame or window
win = Tk()
game = Spy(words)

# Set the size of the window
win.geometry("700x350")


# Define a function to get the output for selected option
def player_4():
    if players_intvar.get() == 4:
        game.players_quantity = 4
        game.spies = 1
        selected = "Spy: 1"
        label.config(text=selected)
        print(f'Players: {game.players_quantity}\nspy: {game.spies}')


def players_num():
    game.players_quantity = players_intvar.get()
    print(game.players_quantity)


def spies_num():
    game.spies = spies_intvar.get()
    print(game.spies)


def is_six():

    selected = "How many Spy?"
    label.config(text=selected)
    s1 = Radiobutton(win, text="1", variable=spies_intvar, value=1, command=spies_num)
    s1.pack(anchor=N)
    s2 = Radiobutton(win, text="2", variable=spies_intvar, value=2, command=spies_num)
    s2.pack(anchor=N)
    s3 = Radiobutton(win, text="3", variable=spies_intvar, value=3, command=spies_num)
    s3.pack(anchor=N)
    b.config(state='disabled')
    button = Button(text='start game')
    button.pack(anchor=N)
    if players_intvar.get() == 4:
        button.config(command=players_num)


def player_6():
    b.config(text='choose spy', command=is_six)


players_intvar = IntVar()
players_intvar.set(4)

spies_intvar = IntVar()
spies_intvar.get()

Label(text="How many Players want to play?:", font=('Aerial 11')).pack()

# Define radiobutton for each options


player1 = Radiobutton(win, text="4", variable=players_intvar, value=4, command=player_4)
player1.pack(anchor=N)

player2 = Radiobutton(win, text="6", variable=players_intvar, value=6, command=players_num)
player2.pack(anchor=N)

player3 = Radiobutton(win, text="8", variable=players_intvar, value=8, command=players_num)
player3.pack(anchor=N)

spy1 = Radiobutton(win, text="1", variable=spies_intvar, value=1, command=spies_num)
spy2 = Radiobutton(win, text="2", variable=spies_intvar, value=2, command=spies_num)
spy3 = Radiobutton(win, text="3", variable=spies_intvar, value=3, command=spies_num)

button = Button(text='Start')
button.pack(anchor=N)

# Define a label widget
label = Label(win)
label.pack()

win.mainloop()
