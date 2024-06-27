from settings import *
from tetris import *
import sys

class App:
    def __init__(self):
        pg.init() #Initializes Pygame
        pg.display.set_caption("Tetris") #Adds name to window
        self.screen = pg.display.set_mode(FIELD_RES) #Sets the window size to the resolution
        self.clock = pg.time.Clock()
        self.set_timer()
        self.tetris = Tetris(self) #Handles the game logic

    def set_timer(self):
        self.user_event = pg.USEREVENT + 0
        self.anim_trigger = False
        pg.time.set_timer(self.user_event, ANIM_TIME_INTERVAL)

    def update(self): #Method used to update the game at a given FPS
        self.tetris.update()
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=FIELD_COLOR) #Clears previous generated frames
        self.tetris.draw()
        pg.display.flip() #Generates a new frame

    def check_events(self):
        self.anim_trigger = False
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE): #Checks if the window was closed the escape key or the escape key was pressed.
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(key_pressed=event.key)
            elif event.type == self.user_event:
                self.anim_trigger = True

    def run(self):
        while True:
            self.check_events()
            self.update()
            self.draw()


if __name__ == "__main__":
    app = App()
    app.run()