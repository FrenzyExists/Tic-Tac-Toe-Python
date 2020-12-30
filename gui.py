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

        if option_game.hover(mouse_x, mouse_y):
            if is_clicking:
                options()

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
    running:bool = True

    fonty=font.get_default_font()

    music_slider = Slider(100, 100, 100)
    sfx_slider = Slider(100, 150, 100)
    fullscreen_button = Button(100, 30, 200, 200, text="Fullscreen")
    return_button = Button(140, 30, 400, 400, text="Back to Menu")

    is_clicking = False

    while running:
        mouse_x, mouse_y = mouse.get_pos()
        
        # Background, game is meant to be simple, don't judge me
        screen.fill((0, 0, 0))

        if return_button.hover(mouse_x, mouse_y):
            if is_clicking:
                running = False
                break

        # Event Loop
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    is_clicking = True
                
            else: is_clicking = False

            music_slider.get_input(event)
            sfx_slider.get_input(event)
        
        # Draw text
        # screen.blit(font.Font(fonty, 24).render("Pause ", 0, (22,67,99)), (132, 230))
        screen.blit(font.Font(fonty, 24).render("Options", 0, (255, 240, 230)), ( int(WINDOWSIZE[0]/2 ), 20))
        screen.blit(font.Font(fonty, 24).render("Music", 0, (255, 240, 230)), (40, 70))
        screen.blit(font.Font(fonty, 24).render("Sound Effects", 0, (255, 240, 230)), (40, 110))

        # Draw Widgets
        music_slider.draw(screen)
        sfx_slider.draw(screen)
        return_button.draw(screen)
        fullscreen_button.draw(screen)



        main_screen.blit(screen, (0,0))
        
        display.update()
        CLOCK.tick(30)

# Select Player (just imagine cpu VS cpu)
def select_player():
    running:bool = True


# Pause menu thingy
def pause():
    option_game = Button(120, 40, 40, 250, "Options",  text_color=COLORS["text"])
    back_to_menu_game = Button(120, 40, 40, 420, "Back to Menu",  text_color=COLORS["text"])


    fonty=font.get_default_font()

    running:bool = True
    while running:
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_SPACE:
                    running = False
                    break

        screen.blit(font.Font(fonty, 24).render("Pause ", 0, (22,67,99)), (132, 230))
        main_screen.blit(screen, (0,0))
        display.update()
        CLOCK.tick(30)

# game
def main():
    running:bool = True

    screen.fill(COLORS["background"])
    test = Grid(100, 70, 300, 300, "3x3")

    fonty=font.get_default_font()    

    while running:
        mouse_x, mouse_y = mouse.get_pos()

        # Check all events
        for ev in event.get():
            if ev.type == QUIT:
                exit()
            if ev.type == KEYDOWN:
                if ev.key == K_ESCAPE:
                    exit()
                if ev.key == K_SPACE:
                    pause()
 
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    is_clicking = True
            else:
                is_clicking = False

        test.draw(screen)

        screen.blit(font.Font(fonty, 60).render("X", 0, (22,67,99)), (test.x+30, test.y+30))

        main_screen.blit(screen, (0, 0))
        display.update()
        CLOCK.tick(30)


# Init
if __name__ == '__main__':
    menu()


