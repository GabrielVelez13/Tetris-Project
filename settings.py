import pygame as pg

FPS = 60
FIELD_COLOR = (38, 43, 58)

vec = pg.math.Vector2

ANIM_TIME_INTERVAL = 150  # milliseconds

# Tetris is composed of a grid of 10 * 20 tiles
TILE_SIZE = 50
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RES = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE  # Tuple of the number of tiles that must be displayed

INIT_POS_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)  # displays where the tetrmino will be places (TOP MIDDLE)

MOVE_DIRECTIONS = {
    'left': vec(-1, 0),
    'right': vec(1, 0),
    'down': vec(0, 1),
}

# Holds the postition of each block of tetrominoes
TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -2), (0, -1)],
}
