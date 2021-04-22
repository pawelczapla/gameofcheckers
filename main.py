import pygame
from checkers.constants import WIDTH, HEIGHT, square_size, WHITE
from checkers.game import Game
from minimax.algorithm import minimax
from checkers.toolbar import root

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Checkers')


def get_mouse_coords(pos):
    x, y = pos
    row = y // square_size
    col = x // square_size
    return row, col


def main():
    run = True
    new_game = Game(WIN)

    while run:
        if not new_game.human_player:
            if new_game.turn == WHITE:
                value, new_board = minimax(new_game.get_board(), 4, WHITE, new_game)
                new_game.algorithm_move(new_board)

        if new_game.winner() is not None:
            print(new_game.winner() + '\n Press new game or exit the application')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_coords(pos)
                new_game.select(row, col)
        root.update()
        new_game.update()
    pygame.quit()


main()
