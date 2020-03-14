import numpy as np

def create_board():
    board = np.zeros((6,7))
    return board


game_over = False
board = create_board()
turn = 0

while (not game_over):

    if(turn==0):
        selection = int(input("Player 1 make your selection(0-6)!: "))
        print(selection)
        print(type(selection))
