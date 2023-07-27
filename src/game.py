from src.index import store
class Game:
    def __init__(self):
        self._id_num = len(store['games'])+1
        store['games'][self.id_num] = self     
    
    @property
    def id_num(self):
        return self._id_num
    
    @id_num.setter
    def id_num(self, id_num):
        self._id_num = id_num

    def welcome_screen(self):
        print("Welcome to Sudoku")
        print("""
        The object of this game is to 
        complete the grid using numbers 
        1-9. A number may NOT repeat 
        itself in any row, column, or box.
        """)
        
