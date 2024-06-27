from settings import *
from tetromino import *


class Tetris:
    def __init__(self, app):
        self.app = app
        self.sprite_group = pg.sprite.Group()  # creates a sprite group
        self.field_array = self.get_field_array()
        self.tetromino = Tetromino(self)

    def check_full_lines(self):
        row = FIELD_HEIGHT - 1
        for y in range(FIELD_HEIGHT - 1, -1, -1):
            for x in range(FIELD_WIDTH):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x,y)

            if sum(map(bool, self.field_array[y])) < FIELD_WIDTH:
                row -= 1
            else:
                for x in range(FIELD_WIDTH):
                    self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def get_field_array(self):
        return [[0 for x in range(FIELD_WIDTH)] for y in range(FIELD_HEIGHT)]

    def check_tetromino_landing(self):
        if self.tetromino.is_landing:
            self.put_tetromino_blocks_in_array()
            self.tetromino = Tetromino(self)

    def control(self, key_pressed):
        if key_pressed == pg.K_LEFT:
            self.tetromino.move(direction='left')
        elif key_pressed == pg.K_RIGHT:
            self.tetromino.move(direction='right')
        elif key_pressed == pg.K_DOWN:
            self.tetromino.move(direction='down')
        elif key_pressed == pg.K_UP:
            self.tetromino.rotate()

    def draw_field(self):
        for x in range(FIELD_WIDTH):  # 10 horizontal blocks
            for y in range(FIELD_HEIGHT):  # 20 vertical blocks
                pg.draw.rect(self.app.screen, 'black', (x * TILE_SIZE, y * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def draw(self):
        self.draw_field()
        self.sprite_group.draw(self.app.screen)

    def update(self):
        if self.app.anim_trigger:
            self.check_full_lines()
            self.tetromino.update()
            self.check_tetromino_landing()
        self.sprite_group.update()
