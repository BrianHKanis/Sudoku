from src.index import store
from src.board import Board
from src.player import Player

class Turn:
    def __init__(self, board, box, cell, val):
        self._id_num = len(store['turns'])+1
        #self._player = board.player
        self._board = board
        #self._selected_square = selected_square
        self._val = val
        self.box = box
        self.cell = cell
        store['turns'][self.id_num] = self

    @property
    def id_num(self):
        return self._id_num
    @id_num.setter
    def id_num(self, id_num):
        self._id_num = id_num
    
    # @property
    # def player(self):
    #     return self._player
    # @player.setter
    # def player(self, player):
    #     self._player = player

    @property
    def board(self):
        return self._board
    @board.setter
    def board(self, board):
        self._board = board

    # @property
    # def selected_square(self):
    #     return self._selected_square
    # @selected_square.setter
    # def selected_square(self, selected_square):
    #     self._selected_square = selected_square
    
    @property
    def val(self):
        return self._val
    @val.setter
    def val(self, val):
        self._val = val
    