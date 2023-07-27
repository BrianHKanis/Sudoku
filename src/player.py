from src.game import Game
from src.index import store

class Player:
    def __init__(self, game, name):
        self._id_num = len(store['players'])+1
        self._game = game
        self._name = name
        store['players'][self.id_num] = self

    # Get/Set player.id_num
    @property
    def id_num(self):
        return self._id_num
    @id_num.setter
    def id_num(self, id_num):
        self._id_num = id_num

    # Get/Set player.game
    @property
    def game(self):
        return self._game
    @game.setter
    def game(self, game):
        self._game = game
    
    # Get/Set player.name and capitalize
    @property
    def name(self):
        return self._name.capitalize()
    @name.setter
    def name(self, name):
        self._name = name.capitalize()