import pygame as pg

FPS = 60
FIELD_COLOR = (38, 43, 58)

# Tetris is composed of a grid of 10 * 20 tiles
TILE_SIZE = 50
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 20
FIELD_RES = FIELD_WIDTH * TILE_SIZE, FIELD_HEIGHT * TILE_SIZE #Tuple of the number of tiles that must be displayed
