import random
import time as t

import pygame
from pygame.locals import *

from constants import *

class GameItem:
    """this class allows to create game items"""
    def __init__(self, sprite, name):
        self.x = 0
        self.y = 0
        self.sprite = sprite.convert_alpha()
        self.name = name


class RunningMap:
    """this class handles the loading of the map from a txt file, a places all the items and the guardian on it"""
    def __init__(self):
        self.r_map = []
        self.window = pygame.display.set_mode((450, 450))
        self.needle = GameItem(needle, "needle")
        self.ether = GameItem(ether, "ether")
        self.tube = GameItem(tube, "tube")
        self.game_items = [self.ether, self.tube, self.needle]
        self.guard_position = (420, 420)

    def load_map(self, chosen_map):
        """Function that loads the map from a file"""
        with open(chosen_map, "r") as f:
            line = []
            rmap = []
            for c in f.read():
                if c != "\n":
                    line.append(c)
                else:
                    rmap.append(line)
                    line = []
        self.r_map = rmap

    def display_end(self, dk):
        """function that displays the end screen"""
        if dk.win:
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
                if self.r_map[x][y] != "W" and (g_item.x, g_item.y) not in placed:
                    g_item.x = y * 30
                    g_item.y = x * 30
                    placed.append((g_item.x, g_item.y))
                    break
        
    def place_guardian(self):
        """function that places the guardian on the maps"""
        x = random.randrange(0, 31, 30)
        y = random.randrange(0, 61, 30)
        self.guard_position = (420 - x, 420 - y)

    def disply_map(self):
        """function that displays the maps, the items and the guardian"""
        self.window.blit(background.convert(), (0, 0))
        self.window.blit(end.convert_alpha(), (self.guard_position))
        x = 0
        y = 0
        _wall = wall.convert()
        for line in self.r_map:
            for sprite in line:
                if sprite == "W":
                    self.window.blit(wall.convert(), (x, y))
                x += 30
                if x == 450:
                    y += 30
                    x = 0
        for g_item in self.game_items:
            self.window.blit(g_item.sprite, (g_item.x + 7, g_item.y))


    
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
            if self.y == 420:
                return
            if self.move_possible(0, 30, my_map):
                self.y += 30
        if key == K_UP:
            if self.y == 0:
                return
            if self.move_possible(0, -30, my_map):
                self.y += -30
        if key == K_RIGHT:
            if self.x == 420:
                return
            if self.move_possible(30, 0, my_map):
                self.x += 30
        if key == K_LEFT:
            if self.x == 0:
                return
            if self.move_possible(-30, 0, my_map):
                self.x += -30
        self.collect_item(my_map)
        self.check_win(my_map)

    def display_list(self, my_map):
        """function that allows to display the list of collected items from the player"""
        listbg = list_bg.convert()
        listbg.set_alpha(90)
        my_map.window.blit(listbg, (0, 350))
        if len(self.collected_items) < 3:
            for i, item in enumerate(self.collected_items):
                my_map.window.blit(item.sprite, (7, i * 40 + 360))
        else:
            my_map.window.blit(syringe.convert_alpha(), (0, 375))
        
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
        case = my_map.r_map[(self.y + y) // 30][(self.x + x) // 30]
        if case != 'W':
            return True

    def display_MC(self, my_map):
        my_map.window.blit(self.sprite, (self.x, self.y))

