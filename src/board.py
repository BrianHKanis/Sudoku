from src.game import Game
from src.player import Player
from src.square import Square
from src.index import store
import random

remove_amounts = {'E': [16, 31], 'M': [31, 46], 'H': [46, 61]}

class Board:
    def __init__(self, player, game):
        self._id_num = len(store['boards'])+1
        self._game = game
        self._player = player
        # self._dificulty = dificulty
        store['boards'][self.id_num] = self

    @property
    def id_num(self):
        return self._id_num
    @id_num.setter
    def id_num(self, id_num):
        self._id_num = id_num

    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        self._game = game

    @property
    def player(self):
        return self.player
    @player.setter
    def player(self, player):
        self.player = player      

    
    # # Gets/Sets single character string to full string for dificulty. Ex.) 'E' -> 'Easy'
    # @property
    # def dificulty(self):
    #     return self._dificulty
    # @dificulty.setter
    # def dificulty(self, dificulty):
    #     self._dificulty = dificulties[dificulty.capitalize()]


    # Borrowed and adapted to OOP
    def create_answer(self):
        self.answer = [[(i + k) % 9 + 1 for i in range(1, 10)] for k in range(9)] # Creates a self.answer where each row counts to 9 such that no row contains more than one kind of each number. You can run this separately to see what it generates.
        random.shuffle(self.answer) # Shuffles this list of lists
        self.answer = [[self.answer[x][y] for x in range(9)] for y in range(9)] # Reads each row and puts it into a column. (basically rotates it to its side)
        random.shuffle(self.answer) # Shuffles this list again but while its on its side
        return self.answer

    def initialize_dificulty(self):
        self.dificulty = (input("What dificulty would you like to play? (E)asy, (M)edium or (H)ard: ")).capitalize()
        self.remove_amount = random.randint(remove_amounts[self.dificulty][0], remove_amounts[self.dificulty][1])
        return self.remove_amount

    def start(self):
        h, w, r = len(self.answer), len(self.answer[0]), []
        spaces = [[x, y] for x in range(h) for y in range(w)]
        for k in range(self.remove_amount):
            r = random.choice(spaces)
            self.answer[r[0]][r[1]] = ' '
            spaces.remove(r)
        self.start = self.answer
        self.layout = self.start
        return self.start
    
    def create_squares(self):
        for box in range(0, 9):
            for cell in range(0, 9):
                self.layout[box][cell] = Square(self.layout[box][cell])
        return f"{(len(store['squares']))} squares made"
        
    def update_cell(self, box_num, cell_num, value):
        self.layout[box_num-1][cell_num-1].val = value

    # Display self.answer to change --> current
    def display(self):
        print(' |-----------| |-----------| |-----------|')
        # First Row
        for b in range(0, 3):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Second Row   
        for b in range(0, 3):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')    
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Third Row
        for b in range(0, 3):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |-----------| |-----------| |-----------|')
        print(' |-----------| |-----------| |-----------|')

        # Fourth Row
        for b in range(3, 6):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Fith Row
        for b in range(3, 6):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Sixth Row
        for b in range(3, 6):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |-----------| |-----------| |-----------|')
        print(' |-----------| |-----------| |-----------|')

        # Seventh Row
        for b in range(6, 9):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Eighth Row
        for b in range(6, 9):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Nineth Row
        for b in range(6, 9):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].val), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')




    def display_id(self):
        print(' |-----------| |-----------| |-----------|')
        # First Row
        for b in range(0, 3):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Second Row   
        for b in range(0, 3):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')    
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Third Row
        for b in range(0, 3):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |-----------| |-----------| |-----------|')
        print(' |-----------| |-----------| |-----------|')

        # Fourth Row
        for b in range(3, 6):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Fith Row
        for b in range(3, 6):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Sixth Row
        for b in range(3, 6):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |-----------| |-----------| |-----------|')
        print(' |-----------| |-----------| |-----------|')

        # Seventh Row
        for b in range(6, 9):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Eighth Row
        for b in range(6, 9):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Nineth Row
        for b in range(6, 9):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].id_num), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')


    def display_xy(self):
        print(' |-----------| |-----------| |-----------|')
        # First Row
        for b in range(0, 3):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Second Row   
        for b in range(0, 3):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')    
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Third Row
        for b in range(0, 3):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |-----------| |-----------| |-----------|')
        print(' |-----------| |-----------| |-----------|')

        # Fourth Row
        for b in range(3, 6):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Fith Row
        for b in range(3, 6):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Sixth Row
        for b in range(3, 6):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |-----------| |-----------| |-----------|')
        print(' |-----------| |-----------| |-----------|')

        # Seventh Row
        for b in range(6, 9):
            for r in range(0, 3):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Eighth Row
        for b in range(6, 9):
            for r in range(3, 6):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')
        # Nineth Row
        for b in range(6, 9):
            for r in range(6, 9):
                print(' | ' + str(self.layout[b][r].row) + ',' + str(self.layout[b][r].column), end='')
            print(' |', end='')
        print('\n |---+---+---| |---+---+---| |---+---+---|')