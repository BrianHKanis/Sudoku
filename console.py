from src.services.play_game import *
from src.index import *
import os
game, player = welcome()
game_setup = True
while game_setup == True:
    #layout = create_layout_of_squares()
    #build_first_row(layout)
    #build_second_row(layout)
    #build_third_row(layout)
    #build_fourth_row(layout)
    #build_fifth_row(layout)
    #layout = establish_layout_with_dificulty(empty_layout, dificulty)
    board = board_setup(game, player)
    while board:
        os.system('clear')
        board.display()
        make_move(board)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # while not validate_layout(layout):
    # else:
        # approved_layout = validate_layout(layout)
    # board = Board(game, player, layout, dificulty)
    # board.display()