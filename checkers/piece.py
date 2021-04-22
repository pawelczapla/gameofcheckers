from .constants import WHITE, square_size, crown, white_man, black_man


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.x = 0
        self.y = 0
        self.color = color
        self.king = False
        self.calculate_position()

    def calculate_position(self):
        self.x = square_size * self.col + square_size // 2
        self.y = square_size * self.row + square_size // 2

    def make_king(self):
        self.king = True
    
    def draw(self, win):
        if self.color == WHITE:
            win.blit(white_man, (self.x - white_man.get_width()//2, self.y - white_man.get_height()//2))
        else:
            win.blit(black_man, (self.x - black_man.get_width()//2, self.y - black_man.get_height()//2))
        if self.king:
            win.blit(crown, (self.x - crown.get_width()//2, self.y - crown.get_height()//2))

    def move(self, row, col):
        self.row = row
        self.col = col
        self.calculate_position()
