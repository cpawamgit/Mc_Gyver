#! env_mcgyver/bin/python

import pygame
from pygame.locals import *

from constants import *
from classes import RunningMap
from classes import CharacterDK

pygame.init()
quit_game = False

def menu():
    global quit_game
    menu = pygame.display.set_mode((450, 450))
    menu_image = home_screen.convert()
    menu.blit(menu_image, (0, 0))

    run = True
    while run:
        if quit_game == True:
            break
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    run = False
                    quit_game = True
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    run = False
                    game("map1.txt")
        if run:
            pygame.display.flip()
        continue

def game_loop(my_map, dk):
    global quit_game
    diplay_list = False
    run = True
    while run:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                    run = False
                    quit_game = True
                    break
            if event.type == KEYDOWN:
                if event.key == K_m:
                    run = False
                    menu()
                    break
                if event.key == K_TAB:
                    diplay_list = True
                else:
                    dk.move_DK(event.key, my_map)
            if event.type == KEYUP:
                if event.key == K_TAB:
                    diplay_list = False
        if run:
            my_map.disply_map()
            dk.display_DK(my_map)
            if diplay_list:
                dk.display_list(my_map)
            pygame.display.flip()
        if dk.win or dk.loose:
            run = False
            my_map.display_end(dk)
        continue

def game(chosen_map):
    my_map = RunningMap()
    my_map.load_map(chosen_map)
    my_map.place_items()
    dk = CharacterDK()
    game_loop(my_map, dk)
    menu()
    #essayer d'implémenter une sortie propre du programme (return 0)

menu()
