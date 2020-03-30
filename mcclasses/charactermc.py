import random

import pygame
from pygame.locals import *

from .constants import *

class CharacterMC:
    """this class allows to create the player character, it handles its controls, and chacks if the player has won or loose"""
    def __init__(self):
        self.x = 0
        self.y = 0
        self.sprite = mc_gyver.convert_alpha()
        self.win = False
        self.loose = False
        self.collected_items = []

    def move_MC(self, key, my_map):
        """function that handles the movement of the player character, and checks if the player can move toward the chosen direction"""
        if key == K_DOWN:
            if self.y == map_size - sprite_size:
                return
            if self.move_possible(0, sprite_size, my_map):
                self.y += sprite_size
        if key == K_UP:
            if self.y == 0:
                return
            if self.move_possible(0, -sprite_size, my_map):
                self.y += -sprite_size
        if key == K_RIGHT:
            if self.x == map_size - sprite_size:
                return
            if self.move_possible(sprite_size, 0, my_map):
                self.x += sprite_size
        if key == K_LEFT:
            if self.x == 0:
                return
            if self.move_possible(-sprite_size, 0, my_map):
                self.x += -sprite_size
        self.collect_item(my_map)
        self.check_win(my_map)

    def display_list(self, my_map):
        """function that allows to display the list of collected items from the player"""
        listbg = list_bg.convert()
        listbg.set_alpha(90)
        my_map.window.blit(listbg, (0, 350))
        if len(self.collected_items) < 3:
            for i, item in enumerate(self.collected_items):
                my_map.window.blit(item.sprite, (15, i * 40 + 360)) #those values have been chosen to center the items in the list
        else:
            my_map.window.blit(syringe.convert_alpha(), (0, 375)) #those values place the list background to the bottom left corner
        
    def check_win(self, my_map):
        """function that checks the win or loose condition"""
        if (self.x, self.y) == my_map.guard_position:
            if len(self.collected_items) == 3:
                self.win = True
            else:
                self.loose = True

    def collect_item(self, my_map):
        """function that checks if the player has collect an item depending on their position"""
        for i, item in enumerate(my_map.game_items):
            if self.x == item.x and self.y == item.y:
                self.collected_items.append(my_map.game_items.pop(i))

    def move_possible(self, x, y, my_map):
        """function that checks if the movement toward the choosen direction is possible or not"""
        case = my_map.r_map[(self.y + y) // sprite_size][(self.x + x) // sprite_size]
        if case != '#':
            return True

    def display_MC(self, my_map):
        my_map.window.blit(self.sprite, (self.x, self.y))