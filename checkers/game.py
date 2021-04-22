import pygame
from .constants import RED, WHITE, square_size, circle
from checkers.board import Board
from checkers.toolbar import root, single, multi, newgame
from tkinter import *
import tkinter as tk


class Game:
    def __init__(self, win):
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.human_player = False
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.display_buttons()

    def multiplayer(self):
        self.human_player = True

    def singleplayer(self):
        self.human_player = False

    def display_buttons(self):
        game_reset = tk.Button(root, text='New Game ', image=newgame, compound=TOP, font='Raleway', command=self.reset,
                               relief=GROOVE)
        game_reset.place(relx=0.2, rely=0.6)
        multiplayer = tk.Button(root, text='Multiplayer  ', image=multi, compound=TOP, font='Raleway',
                                command=self.multiplayer, relief=GROOVE)
        multiplayer.place(relx=0.2, rely=0.72)
        singleplayer = tk.Button(root, text='Singleplayer', image=single, compound=TOP, font='Raleway',
                                 command=self.singleplayer, relief=GROOVE)
        singleplayer.place(relx=0.2, rely=0.84)

    def winner(self):
        return self.board.winner()

    def reset(self):
        self._init()

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_legal_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            self.win.blit(circle, (col * square_size + 25, row * square_size + 25))

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def get_board(self):
        return self.board

    def algorithm_move(self, board):
        self.board = board
        self.change_turn()
