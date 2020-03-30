import sys
import random
import time as t

import pygame
from pygame.locals import *

from .constants import *
from .gameitem import GameItem

class RunningMap:
    """this class handles the loading of the map from a txt file, a places all the items and the guardian on it"""
    def __init__(self):
        self.r_map = []
        self.window = pygame.display.set_mode((map_size, map_size))
        self.needle = GameItem(needle, "needle")
        self.ether = GameItem(ether, "ether")
        self.tube = GameItem(tube, "tube")
        self.game_items = [self.ether, self.tube, self.needle]
        self.guard_position = (420, 420)

    def load_map(self, chosen_map):
        """Function that loads the map from a file"""
        with open(chosen_map, "r") as f:
            rmap = [[c for c in s] for s in f.read().split("\n")]
        self.r_map = rmap

    def display_end(self, mc):
        """function that displays the end screen"""
        if mc.win:
            self.window.blit(you_win.convert(), (0, 0))
            pygame.display.flip()
            t.sleep(2)
        else:
            self.window.blit(you_loose.convert(), (0, 0))
            pygame.display.flip()
            t.sleep(2)

    def place_items(self):
        """function that places the items on the maps"""
        random.shuffle(self.game_items)
        placed = []
        for g_item in self.game_items:
            while True:
                x = random.randint(1, 11)
                y = random.randint(0, 14)
                if self.r_map[x][y] != "#" and (y * sprite_size, x * sprite_size) not in placed:
                    g_item.x = y * sprite_size
                    g_item.y = x * sprite_size
                    placed.append((g_item.x, g_item.y))
                    break
        
    def place_guardian(self):
        """function that places the guardian on a 3*2 rectangle on the bottom right off the map"""
        x = random.randrange(0, sprite_size + 1, sprite_size)
        y = random.randrange(0, sprite_size * 2 + 1, sprite_size)
        self.guard_position = (map_size - sprite_size - x, map_size - sprite_size - y)

    def disply_map(self):
        """function that displays the maps, the items and the guardian"""
        self.window.blit(background.convert(), (0, 0))
        self.window.blit(end.convert_alpha(), (self.guard_position))
        x = 0
        y = 0
        _wall = wall.convert()
        for line in self.r_map:
            for sprite in line:
                if sprite == "#":
                    self.window.blit(wall.convert(), (x, y))
                x += sprite_size
                if x == map_size:
                    y += sprite_size
                    x = 0
        for g_item in self.game_items:
            self.window.blit(g_item.sprite, (g_item.x + 7, g_item.y))