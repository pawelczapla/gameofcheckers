import pygame

# Dimensions
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
square_size = 100

# Colors
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)

# Assets
circle = pygame.image.load('assets/circle.png')
background = pygame.image.load('assets/black.jpg')
tile = pygame.image.load('assets/white.png')
white_man = pygame.image.load('assets/white_man.png')
black_man = pygame.image.load('assets/black_man.png')
crown = pygame.transform.scale(pygame.image.load('assets/crown.png'), (62, 62))
