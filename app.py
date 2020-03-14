import numpy as np

NUM_ROW = 6
NUM_COL = 7

def create_board():
    board = np.zeros((NUM_ROW,NUM_COL))
    return board

def is_collumn_valid(board, collumn):
    return board[NUM_ROW - 1][collumn] == 0

def drop_move(board, row, collumn, piece):
    board[row][collumn] = piece

def next_open_row(board, collumn):
    for r in range(NUM_ROW):
        if(board[r][collumn] == 0):
            return r

def print_board(board):
    print(np.flip(board,0))
def end_game(board, piece):
    for c in range(NUM_COL - 3):
        for r in range(NUM_ROW):
            #Horizontal locations for win
            if (board[r][c]==piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece):
                return True
            #Vertical locations for win
            elif(board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] and board[r+3][c] == piece):
                return True
            elif(board[r][c] == piece and board[r+1][c+1] == [piece] and board [r+2][c+2] == piece and board[r+3][c+3] == piece)
                return True
            #Check if it works!!!!




game_over = False
board = create_board()
print_board(board)
turn = 0

while (not game_over):

    if(turn==0):
        selection = int(input("Player 1 make your selection(0-6)!: "))

        if(is_collumn_valid(board,selection) == True):
            row = next_open_row(board,selection)
            drop_move(board,row,selection,1)

    else:
        selection = int(input("Player 2 make your selection(0-6)!: "))
        if(is_collumn_valid(board,selection) == True):
            row = next_open_row(board,selection)
            drop_move(board,row,selection,2)
    print_board(board)
    turn += 1
    turn = turn % 2
