import numpy as np
import pygame
import sys
import math

NUM_ROW = 6
NUM_COL = 7
SQUARE_SIZE = 100
WIDTH = NUM_COL * SQUARE_SIZE
HEIGHT = (NUM_ROW + 1) * SQUARE_SIZE
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255,0,0)
YELLOW = (255,255,0)
RADIUS = int(SQUARE_SIZE / 2 - 5)


def create_board():
    board = np.zeros((NUM_ROW, NUM_COL))
    return board


def is_collumn_valid(board, collumn):
    return board[NUM_ROW - 1][collumn] == 0


def drop_move(board, row, collumn, piece):
    board[row][collumn] = piece


def next_open_row(board, collumn):
    for r in range(NUM_ROW):
        if (board[r][collumn] == 0):
            return r


def print_board(board):
    print(np.flip(board, 0))


def end_game(board, piece):
    for c in range(NUM_COL - 3):
        for r in range(NUM_ROW):
            # Horizontal locations for win
            if (board[r][c] == piece and board[r][c + 1] == piece and board[r][c + 2] == piece and board[r][
                c + 3] == piece):
                return True

    for c in range(NUM_COL):
        for r in range(NUM_ROW - 3):
            if (board[r][c] == piece and board[r + 1][c] == piece and board[r + 2][c] and board[r + 3][c] == piece):
                return True

    for c in range(NUM_COL - 3):
        for r in range(NUM_ROW - 3):
            if (board[r][c] == piece and board[r + 1][c + 1] == [piece] and board[r + 2][c + 2] == piece and
                    board[r + 3][c + 3] == piece):
                return True

    for c in range(NUM_COL):
        for r in range(3, NUM_ROW):
            if (board[r][c] == piece and board[r - 1][c + 1] == [piece] and board[r - 2][c + 2] == piece and
                    board[r - 3][c + 3] == piece):
                return True


def draw_board(board):
    for c in range(NUM_COL):
        for r in range(NUM_ROW):
            pygame.draw.rect(screen, BLUE, (c * SQUARE_SIZE, r * SQUARE_SIZE + SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE),
                             0)

            pygame.draw.circle(screen, BLACK, (
                int(c * SQUARE_SIZE + SQUARE_SIZE / 2), int(r * SQUARE_SIZE + SQUARE_SIZE + SQUARE_SIZE / 2)), RADIUS)

    for c in range(NUM_COL):
        for r in range(NUM_ROW):
            if board[r][c] == 1:
                pygame.draw.circle(screen, RED, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                   RADIUS)
            elif board[r][c] == 2:
                pygame.draw.circle(screen, YELLOW, (
                    int(c * SQUARE_SIZE + SQUARE_SIZE / 2), HEIGHT - int(r * SQUARE_SIZE + SQUARE_SIZE / 2)),
                                 RADIUS)


    pygame.display.update()


game_over = False
board = create_board()
print_board(board)
turn = 0

pygame.init()

size = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()

winfont = pygame.font.SysFont("monospace",75)

while (not game_over):

    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,WIDTH,SQUARE_SIZE),0)
            posx = event.pos[0]
            if(turn == 0):
                pygame.draw.circle(screen,RED,(posx,int(SQUARE_SIZE/2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW,(posx, int(SQUARE_SIZE/2)),RADIUS)
            pygame.display.update()
        if (event.type == pygame.MOUSEBUTTONDOWN):


            if (turn == 0):
                posx = event.pos[0]
                selection = int(math.floor(posx / SQUARE_SIZE))

                if (is_collumn_valid(board, selection) == True):
                    row = next_open_row(board, selection)
                    drop_move(board, row, selection, 1)

                    if (end_game(board, 1) == True):
                        pygame.draw.rect(screen,(0,0,WIDTH,SQUARE_SIZE))
                        label = winfont.render("PLAYER 1 WINS!",1,RED)
                        screen.blit(label,(40,10))
                        game_over = True

            else:
                posx = event.pos[0]
                selection = int(math.floor(posx / SQUARE_SIZE))
                if (is_collumn_valid(board, selection) == True):
                    row = next_open_row(board, selection)
                    drop_move(board, row, selection, 2)

                    if (end_game(board, 2) == True):
                        pygame.draw.rect(screen, (0, 0, WIDTH, SQUARE_SIZE))
                        label = winfont.render("PLAYER 2 WINS!", 1, YELLOW)
                        screen.blit(label, (40, 10))
                        game_over = True

        print_board(board)
        draw_board(board)
        turn += 1
        turn = turn % 2

        if game_over:

            pygame.time.wait(3000)
