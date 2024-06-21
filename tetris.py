import pygame

from settings import *
from tetromino import *
import math

class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()
        self.tetromino = Tetromino(self)


    def draw_field(self):
        for x in range(FIELD_WIDTH): #10 horizontal blocks
            for y in range(FIELD_HEIGHT): #20 vertical blocks
                pg.draw.rect(self.app.screen, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def draw(self):
        self.draw_field()
        self.sprite_group.draw(self.app.screen)

    def update(self):
        self.tetromino.update()
        self.sprite_group.update()

