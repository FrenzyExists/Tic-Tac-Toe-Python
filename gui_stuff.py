#!/usr/bin/env python3

# Pygame gui stuff
#
# //// Hehe ////////////////////////////////////////////////////////////////////////////////////////////////////////     
__author__ = "Frenzy"
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////     

"""
I've used these things at a few trinkets of mine, and I'm not willing to re-invent the damn wheel again
"""

# Load dependencies
import pygame
from pygame.locals import *
from sys import exit

# Initiate Pygame
pygame.init()

# //// Music Library ////////////////////////////////////////////////////////////////////////////////////////////////////////    
def library(target_list, *args):
    for i in args:
        target_list.append(pygame.mixer.Sound(i))

# //// Setting Vol Globally ////////////////////////////////////////////////////////////////////////////////////////////////////////
def set_all_vol(sounds, value):
    for sound in sounds:
        vol = sound.get_volume()
        sound.set_volume(value/100)

def get_all_vol(sounds) -> float:
    n, s = 0, 0
    for sound in sounds:
        n += 1
        s += sound.get_volume()
    return s/n

# From StackOverflow 
def screenshake():
    shk = -1
    for i in range(0, random.randint(3, 5)):
        for x in range(0, 20, random.randint(6, 10)):
            yield (x * shk, 0)
        for x in range(20, 0, random.randint(6, 10)):
            yield (x * shk, 0)
    while True:
        yield (0, 0)

# //// Clear Screen :D ////////////////////////////////////////////////////////////////////////////////////////////////////////
def redrawWindow(surface, fill=(0,0,0), flicker=False):
    surface.fill(fill)
    # for flickering update here :)
    if flicker == True:
        surface.update()

# //// Button //////////////////////////////////////////////////////////////////////////////////////////////////////////
class Button:
    def __init__(self, width, height, x_pos, y_pos, text="", _color=(0, 0, 0), text_color=(40, 40, 40), text_alignment="left", font=pygame.font.get_default_font() ):
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.color = _color
        self.text = text
        self.text_color = text_color
        if type(font) == pygame.font.Font:
            self.font = font
        else:
            self.font = pygame.font.Font(font, 24);

        self.rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.width, self.height)
        self.tx, self.ty = self.font.size(self.text)

        if text_alignment == "center":
            self.x_alignment = int(self.width / 2) - int(self.tx / 2)

        elif text_alignment == "left":
            # self.x_alignment = int(self.width / 6) 
            self.x_alignment = 5

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        surface.blit(self.font.render(self.text, 0, self.text_color),
                    (self.x_pos + self.x_alignment, self.y_pos + int(self.height / 2) - int(self.ty / 2) ))
    def set_color(self, _color):
        self.color = _color

    def set_text_color(self, _color):
        self.text_color = _color

    def hover(self, mouse_x, mouse_y, new_text_color=(0,0,0), new_button_color=(255, 255, 255)):
        temp_color = new_text_color
        temp_text_color = new_button_color
        if self.rect.collidepoint(mouse_x, mouse_y):
            temp_text_color = self.text_color
            temp_color = self.color
            self.color = new_button_color
            self.text_color = new_text_color
            return True
        else:
            self.color = temp_color
            self.text_color = temp_text_color
            return False


# //// Slider //////////////////////////////////////////////////////////////////////////////////////////////////////////
# Note: Some pieces of this code is from AustL's Pygame Widgets module
class Slider:
        def __init__(self, x_pos, y_pos, width, value=0, min_value=0, max_value=99, step=1, height=5, slider_width=10, slider_height=10, bar_color=(200, 200, 200), slider_color=(100, 23, 44)):
            
            # Position of slider and bar on screen
            self.x_pos = x_pos
            self.y_pos = y_pos

            # Bar Dimensions
            self.bar_width = width
            self.bar_height = height

            # Slider Dimensions
            self.slider_width = slider_width
            self.slider_height = slider_height

            # Colors
            self.bar_color = bar_color
            self.slider_color = slider_color

            # Values
            self.min_value = min_value
            self.max_value = max_value
            self.value = value # Start value, also controls slider position in relation of the bar that "holds" it
            self.step = step
            self.hit = False # Checks if is pressed
            
            # Rects
            self.bar_rect = pygame.rect.Rect(self.x_pos, self.y_pos, self.bar_width, self.bar_height)
            self.slider_rect = pygame.rect.Rect(self.x_pos+value, self.y_pos - int(self.bar_height / 2), self.slider_width, self.slider_height)


        def draw(self, surface):
            self.slider_rect.x = self.x_pos + self.value
            pygame.draw.rect(surface, self.bar_color, self.bar_rect)
            pygame.draw.rect(surface, self.slider_color, self.slider_rect)
            

        def get_input(self, event):
            is_pressed = pygame.mouse.get_pressed()[0] # Mousedown
            mouse_x, mouse_y = pygame.mouse.get_pos()
            
            if pygame.mouse.get_pressed()[0]:

                if self.bar_rect.collidepoint(mouse_x, mouse_y):
                    self.hit = True

                if self.hit:
                    self.value = self.round_value( (mouse_x - self.x_pos) / self.bar_width * self.max_value + self.min_value )
                    self.value = max(min(self.value, self.max_value), self.min_value)
            else:
                self.hit = False

        def cotains(self, x, y):
            x_range = 0

        def round_value(self, value):
            return self.step * round(value/self.step)

        def set_bar_color(self, _color):
            self.bar.fill(color)

        def set_slider_color(self, _color):
            self.slider.fill(color)
        
        def get_value(self):
            return self.value


class Grid(pygame.sprite.Sprite):
    def __init__(self,x_pos:float, y_pos:float, width:float, height:float, size:str, color:tuple=(255,255,255), fill_color:tuple=(0,0,0), round_corners=False, inner_grid_h_color=(12,45,90), inner_grid_v_color=(122,45,90), outer_grid=True, outer_grid_color=(44,44,44) ):
        pygame.sprite.Sprite.__init__(self)
        self.x = x_pos
        self.y = y_pos
        self.w = width
        self.h = height

        self.inner_grid_h_color = inner_grid_h_color
        self.inner_grid_v_color = inner_grid_v_color
        self.outer_grid = outer_grid
        self.outer_grid_color = outer_grid_color

        self.dx, self.dy = [int(i) for i in size.lower().split("x")]

        self.color = color
        self.fill = fill_color

        self.corners = round_corners

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = self.x, self.y
        self.border_radius = int( ((self.w+self.h)/2)/12 )

    def draw(self, surface: pygame.Surface):

        # Fill
        pygame.draw.rect(surface, self.color, self.rect)

        rectout = pygame.Surface((self.w+20, self.h+20)).get_rect()
        rectout.x, rectout.y = self.x-10, self.y-10

        horizontal_cellsize = (self.w)/self.dx
        vertical_cellsize = (self.h)/self.dy

        for x in range(1, self.dx):  
        # VERTICAL DIVISION
        
            pygame.draw.line(
            surface, self.inner_grid_v_color,
            # Beginning Point
            (self.x + (horizontal_cellsize*x), self.y + 0 ),
            # Ending Point
            (self.x + horizontal_cellsize*x, self.y+self.h - 0 ), 3)

        for x in range(1, self.dy):
        # HORITZONTAL DIVISION

            pygame.draw.line(
            surface, self.inner_grid_h_color,
            # Beginning Point
            (self.x + self.w - 0, self.y + (vertical_cellsize*x)),
            # Ending Point
            (self.x + 0, self.y + (vertical_cellsize*x)), 3)

        if self.outer_grid == True:
            if self.corners == True:
                pygame.draw.rect(surface, self.outer_grid_color, rectout, 10, self.border_radius)
            else:
                pygame.draw.rect(surface, self.outer_grid_color, rectout, 10, 1)

            
# //// Dot Object ////////////////////////////////////////////////////////////////////////////////////////////////////////
class Dot(pygame.sprite.Sprite):
    def __init__(self, surface, x:float, y:float, width:float, height:float, color:tuple=(255,255,255), dot_color:tuple=(0,0,0)):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.w = width
        self.h = height
        self.surface = surface

        self.color = color
        self.dot_color = dot_color

        self.image = pygame.Surface((self.w, self.h))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.pos_dict = {
            "top": int(self.y + self.h/(10-4)),
            "bottom": int(self.y + self.h - self.h/(10-4)),
            "left": int(self.x + self.w/(10-4)),
            "right":int(self.x + self.w - self.w/(10-4)),
            "center_x": int(self.x + self.w/2),
            "center_y": int(self.y + self.h/2)
        }
        self.dot_r = int(self.w/10)

    def draw(self, position_in_rect:str="default"):
        pygame.draw.rect(self.surface,  self.color, self.rect)
        if position_in_rect == "default":
            pygame.draw.circle(self.surface, self.dot_color, tuple(self.pos_dict[s] for s in "center_x-center_y".split("-")), self.dot_r)
        else:
            pygame.draw.circle(self.surface, self.dot_color, tuple(self.pos_dict[s] for s in position_in_rect.split("-")), self.dot_r)


# //// Fade Screen ////////////////////////////////////////////////////////////////////////////////////////////////////////
def fade(size, surface, fade_color=(0,0,0), delay=5):
    fade_surface = pygame.Surface(size)
    fade_surface.fill(fade_color)
    for alpha in range(300):
        fade_surface.set_alpha(alpha)
        redrawWindow(surface)
        surface.blit(fade_surface, (0, 0))
        pygame.display.update()
        pygame.time.delay(delay)
