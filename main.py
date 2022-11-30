"""
Spy game's Demo
"""

import random

WORDS = ['word1', 'word2', 'word3', 'word4', 'word5']
PLAYERS_LIST = []
SPY = int
GAME_FINISHED = False

# Start game
while not GAME_FINISHED:
    # Create a word
    word = random.choice(WORDS)
    # Add Players and Spies
    players = int(input('How many Players want to play? 4, 6, 8 ====> '))
    if players == 4:
        SPY = 1
    elif players == 6 or 8:
        SPY = int(input('How many Spy? 1, 2, 3 ====> '))
    # Add people
    peoples = players - SPY
    # Create Player list
    for people in range(peoples):
        PLAYERS_LIST.append('People')
    for spy in range(SPY):
        PLAYERS_LIST.append('Spy')
    # Game start
    for turn in range(len(PLAYERS_LIST)):
        choices = random.choice(PLAYERS_LIST)
        people_or_spy = f'You are {choices}'
        if choices == 'People':
            print(f'You are a people!\nThe word is {word}')
        else:
            print('You are a Spy!')
        should_continue = input(f'Press "Inter".\n')
        PLAYERS_LIST.remove(choices)
        print('*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n*\n')
        if len(PLAYERS_LIST) == 0:
            print('The Game has started')
            GAME_FINISHED = True
