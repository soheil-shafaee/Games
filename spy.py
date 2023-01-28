import random


class Spy:
    def __init__(self, word):
        self.players_list = []
        # Player's number
        self.players_quantity = None
        # Peoples
        self.peoples = None
        # Spies
        self.spies = None
        # Create a word
        self.word = random.choice(word)

    def create_player(self):
        # Add Players and Spies
        self.players_quantity = int(input('How many Players want to play? 4, 6, 8 ====> '))
        if self.players_quantity == 4:
            self.spies = 1
        elif self.players_quantity == 6 or 8:
            self.spies = int(input('How many Spy? 1, 2, 3 ====> '))
        self.peoples = self.players_quantity - self.spies

        # Create Players list
        for people in range(self.peoples):
            self.players_list.append('People')

        for spy in range(self.spies):
            self.players_list.append('Spy')
        random.shuffle(self.players_list)
        # Game start
        for turn in range(len(self.players_list)):
            character = random.choice(self.players_list)
            if character == 'People':
                print(f'You are a people!\nThe word is {self.word}')
            else:
                print('You are a Spy!')
            self.players_list.remove(character)

    def still_has_players(self):
        return self.players_quantity < len(self.players_list)
