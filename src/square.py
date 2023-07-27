from src.index import store
from src.index import row_ids, column_ids
import random

class Square:
    def __init__(self, val=' '):
        self._id_num = len(store['squares'])+1
        self._val = val
        # self.box = self.id_to_box()
        # self.row = self.id_to_row()
        # self.column = self.id_to_column()
        store['squares'][self.id_num] = self


    @property
    def id_num(self):
        return self._id_num
    @id_num.setter
    def id_num(self, id_num):
        self._id_num = id_num

    @property
    def val(self):
        return self._val
    @val.setter
    def val(self, val):
        self._val = val


    def fill_square(self):
        print('Please select the box number, cell number, and value you wish to input')
        box, cell = input("Box #, Cell #: ")




    

    # # Indexing positions
    # # Row number
    # def id_to_row(self):
    #     for i in range(0, len(row_ids)):
    #         current_row = row_ids[i]
    #         if self.id_num in current_row:
    #             return i + 1
    # # Column number
    # def id_to_column(self):
    #     for i in range(0, len(column_ids)):
    #         current_column = column_ids[i]
    #         if self.id_num in current_column:
    #             return i + 1
    # # Box number
    # def id_to_box(self): 
    #     if self.id_num in range(1, 10):
    #         return 1
    #     elif self.id_num in range(10, 19):
    #         return 2
    #     elif self.id_num in range(19, 28):
    #         return 3
    #     elif self.id_num in range(28, 37):
    #         return 4
    #     elif self.id_num in range(37, 46):
    #         return 5
    #     elif self.id_num in range(46, 55):
    #         return 6
    #     elif self.id_num in range(55, 64):
    #         return 7
    #     elif self.id_num in range(64, 73):
    #         return 8
    #     elif self.id_num in range(73, 82):
    #         return 9
        # for loop with counter?
    


    # def preset_val(self):
    #     self.val = random.randint(1, 9)
