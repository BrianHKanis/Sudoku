from src.game import Game
from src.player import Player
from src.square import Square
from src.board import Board
from src.turn import Turn
from src.index import store
import random

# Total number of cells = 81 (3x3)x(3x3)
# Range of populated cells per dificuly level.
dificulty_range = {'E': [4, 7], 'M': [3, 6], 'H': [2, 5]}

def welcome():
    game = Game()
    player_name = input("Please type your name: ")
    player = Player(game, player_name)
    print(f"\nHi {player.name}\n")
    game.welcome_screen()
    return game, player

def board_setup(game, player):
    board = Board(player, game)
    board.create_answer()
    board.initialize_dificulty()
    board.start()
    board.create_squares()
    return board


def make_move(board):
    box_num = int(input("Pick a box: "))
    cell_num = int(input("Now pick a cell in that box: "))
    value = int(input("What number would you like here: "))
    while board.layout[box_num-1][cell_num-1].val != ' ':
        print('This cell is occupied, please try again...')
        box_num = int(input("Pick a box: "))
        cell_num = int(input("Now pick a cell in that box: "))
        value = int(input("What number would you like here: "))
    else: 
        board.update_cell(box_num, cell_num, value)
        turn = Turn(board, box_num, cell_num, value)
        return print('Board updated')


# def create_layout_of_squares():
    empty_layout = [[], [], [], [], [], [], [], [], []]
    for box in range(0, 9, 1): # For each of the 9 boxes.
        for i in range(0, 9, 1): # Add 9 square instances.
            empty_layout[box].append(Square()) 
    return empty_layout



# def build_first_row(layout):
    # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # for square_lists in layout:
    #     for square in square_lists:
    #         if square.row == 1:
    #             number = random.choice(numbers)
    #             square.val = number
    #             numbers.remove(number)
    # return layout

# def build_second_row(layout):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    box1_restrictions = []
    box2_restrictions = []
    box3_restrictions = []
    for square_lists in layout:
        for square in square_lists:
            # Restricitons
            if square.box == 1 and square.row == 1:
                    box1_restrictions.append(square.val)
            elif square.box == 2 and square.row == 1:
                    box2_restrictions.append(square.val)
            elif square.box == 3 and square.row == 1:
                    box3_restrictions.append(square.val)           
            # Assignment - First Box
    for square_lists in layout:
        for square in square_lists:
            if square.row == 2 and square.box == 1:
                number = random.choice([number for number in numbers if number not in box1_restrictions])
                square.val = number
                numbers.remove(number)
            # Second Box
            elif square.row == 2 and square.box == 2:
                number = random.choice([number for number in numbers if number not in box2_restrictions])
                square.val = number
                numbers.remove(number) 
            # Third Box
            elif square.row == 2 and square.box == 3:
                number = random.choice(numbers)
                square.val = number
                numbers.remove(number)            
    return layout    

# Sometimes throws error "seq[self._randbelow(len(seq))]"
# when no 
# def build_third_row(layout):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    box1_restrictions = []
    box2_restrictions = []
    box3_restrictions = []
    for square_lists in layout:
        for square in square_lists:
            # Restricitons First
            if square.box == 1:
                if square.row == 1:
                    box1_restrictions.append(square.val)
                elif square.row == 2:
                    box1_restrictions.append(square.val)
            elif square.box == 2:
                if square.row == 1:
                    box2_restrictions.append(square.val)
                elif square.row == 2:
                    box2_restrictions.append(square.val)
            elif square.box == 3:
                if square.row == 1:
                    box3_restrictions.append(square.val)    
                elif square.row == 2:
                    box3_restrictions.append(square.val)
    for square_lists in layout:
        for square in square_lists:                           
            # Assignment - First Box
            if square.box == 1:
                if square.row == 3:
                    number = random.choice([number for number in numbers if number not in box1_restrictions])
                    square.val = number
                    numbers.remove(number)
            elif square.box == 2:
                if square.row == 3:
                    number = random.choice([number for number in numbers if number not in box2_restrictions])
                    square.val = number
                    numbers.remove(number)
            elif square.box == 3:
                if square.row == 3:
                    number = random.choice([number for number in numbers if number not in box3_restrictions])
                    square.val = number
                    numbers.remove(number) 
    return layout   

# def build_fourth_row(layout):
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    column_restrictions = {1: [], 2: [], 3: [], 4: [], 5: [], 6: [], 7: [], 8: [], 9: []}
    for square_lists in layout:
        for square in square_lists:
            # Restricitons First
            column_restrictions[square.column].append(square.val) 
    for square_lists in layout:
        for square in square_lists:                           
            # Assignment - First Box
            if square.row == 4:
                number = random.choice([number for number in numbers if number not in column_restrictions[square.column]])
                square.val = number
                numbers.remove(number)           
    return layout 



# def establish_layout_with_dificulty(squares, dificulty):
#     for box in range(0, 9, 1):
#         number_of_established_squares_per_current_box = random.randint(dificulty_range[dificulty][0], dificulty_range[dificulty][1])
#         index_of_established_squares = random.sample(range(0, 9), number_of_established_squares_per_current_box)
#         # List of non-repeating values to populate cells in each box.
#         random_values = random.sample(range(1, 9), number_of_established_squares_per_current_box)
#         for index in index_of_established_squares:
#             squares[box][index].val = random_values.pop()
#     return squares


# def validate_and_correct_row(layout):
#     for b in range(0, 3):
#         for r in range(0, 3):
#             if layout[b]


# def validate_and_correct_column(layout):
#     pass

# Create a solved puzzle then take away
# percentage solved based on dificulty


# def build_first_column(layout):
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     box_restrictions = []
#     for square_lists in layout:
#         for square in square_lists:
#             # Restricitons
#             if square.row == 1 and square.column == 1:
#                 numbers.remove(square.val) 
#             elif square.row == 1 and square.box == 1 and square.column != 1:
#                 box_restrictions.append(square.val)
#             # Assignment - First Box
#             if square.column == 1 and square.box == 1 and square.row != 1:
#                 number = random.choice([number for number in numbers if number not in box_restrictions])
#                 square.val = number
#                 numbers.remove(number)
#             # Rest of column
#             elif square.column == 1 and square.box != 1 and square.row != 1:
#                 number = random.choice(numbers)
#                 square.val = number
#                 numbers.remove(number)  
#     return layout

# def build_second_column(layout):
#     numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     box1_restrictions = []
#     box2_restrictions = []
#     box3_restrictions = []
#     for square_lists in layout:
#         for square in square_lists:
#             # Restricitons
#             if square.row == 1 and square.column == 2:
#                 numbers.remove(square.val) 
#             elif square.column == 1 and square.box == 1:
#                 box1_restrictions.append(square.val)
#             elif square.column == 1 and square.box == 2:
#                 box2_restrictions.append(square.val)
#             elif square.column == 1 and square.box == 3:
#                 box3_restrictions.append(square.val)           
#             # Assignment - First Box
#             if square.column == 2 and square.box == 1 and square.row != 1:
#                 number = random.choice([number for number in numbers if number not in box1_restrictions])
#                 square.val = number
#                 numbers.remove(number)
#                 breakpoint()
#             # Second Box
#             elif square.column == 2 and square.box == 2:
#                 number = random.choice([number for number in numbers if number not in box2_restrictions])
#                 square.val = number
#                 numbers.remove(number) 
#             # Third Box
#             elif square.column == 2 and square.box == 3:
#                 number = random.choice([number for number in numbers if number not in box3_restrictions])
#                 square.val = number
#                 numbers.remove(number)            
#     return layout


        