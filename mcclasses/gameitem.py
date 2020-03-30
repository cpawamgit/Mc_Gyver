import pygame
from pygame.locals import *

from .constants import *

class GameItem:
    """this class allows to create game items"""
    def __init__(self, sprite, name):
        self.x = 0
        self.y = 0
        self.sprite = sprite.convert_alpha()
        self.name = name