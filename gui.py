#!/usr/bin/env python3

from pygame import *
from pygame.locals import *
import os
import tic_tac_toe as ttt
from gui_stuff import Button, Slider, Grid

# Constants :D
WINDOWSIZE = (640, 470)

COLORS = {
    "button"     : (108, 120, 157),
    "text"       : (41, 69, 97), 
    "coins"      : (81, 148, 214),
    "background" : (214, 194, 81),
    "line"       : (41, 69, 97)
}
COINS = ("O", "X")

# Load Icon
# ICON = image.load("resources/icon.png")

# Load Music
MUSIC_THEME = "resources/music_theme.wav"
MUSIC_GAME = "resources/music_game.wav"

# Load Font
FONT = font.Font("resources/font/BaiJamjuree-Regular.ttf", 30)
FONT_COIN = font.Font("resources/font/BaiJamjuree-SemiBold.ttf", 80)
FONT_TITLE = font.Font("resources/font/BaiJamjuree-Light.ttf", 60)

# Initiate Pygame
init()

# Pygame Base Stuff
CLOCK = time.Clock()
mixer.init()
display.set_caption("Tic Tac Toe")
mouse.set_visible(False)

# Initialize Surfaces
main_screen = display.set_mode(WINDOWSIZE, 0, 32)
screen = main_screen.copy() 


class TicTacToeGrid(Grid):
    def __init__(self, x_pos:float, y_pos:float, width:float, height:float, size:str):
        Grid.__init__(self)
        

    # override
    def draw(self):
        pass

    def insert_coin(self):
        pass


    def set_coin_color(self):
        pass

    def set_grid_color(self):
        pass

    def set_fill_color(self):
        pass


# www.freegamesdl.net
# menu
def menu():
    running:bool = True

    new_game = Button(140, 40, 40, 150, "New Game",  text_color=COLORS["text"])
    option_game = Button(120, 40, 40, 250, "Options",  text_color=COLORS["text"])
    exit_game = Button(120, 40, 40, 420, "Exit",  text_color=COLORS["text"])

    screen.fill(COLORS["background"])

    while running:
        mouse_x, mouse_y = mouse.get_pos()

        if new_game.hover(mouse_x, mouse_y):
            if is_clicking:
                main()
        
        if exit_game.hover(mouse_x, mouse_y):
            if is_clicking:
                exit()

        # Check all events
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    exit()
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    is_clicking = True
            else:
                is_clicking = False

        new_game.draw(screen)
        option_game.draw(screen)
        exit_game.draw(screen)
        main_screen.blit(screen, (0, 0))
        display.update()
        CLOCK.tick(30)


# options.
def options():
    pass

# Select Player (just imagine cpu VS cpu)
def select_player():
    pass


# Pause menu thingy
def pause():
    pass

# game
def main():
    running:bool = True

    screen.fill(COLORS["background"])
    test = Grid(100, 70, 100, 400, "3x10")

    while running:
        mouse_x, mouse_y = mouse.get_pos()

        # Check all events
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    exit()
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    is_clicking = True
            else:
                is_clicking = False

        test.draw(screen)

        main_screen.blit(screen, (0, 0))
        display.update()
        CLOCK.tick(30)


# Init
if __name__ == '__main__':
    menu()


