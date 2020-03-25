#! env/bin/python

"""This programm is a game, called mc_gyver. The purpose is to collect items in a maze, once the player got them

all, mcgyver crafts an syringe. Then meet the guardian to put him asleep, if you meet the guardian without all the items,

the gard will spot you, so you loose.

"""

import pygame
from pygame.locals import *

from constants import *
from classes import RunningMap
from classes import CharacterMC

pygame.init() #initializes the module pygame
quit_game = False #global boolean that can be checked by the menu loop and the game loop

def menu():
    """Function that displays the menu and check the event related to it"""
    global quit_game
    display_controls = False
    menu = pygame.display.set_mode((450, 450)) #initializing the menu surface
    menu_image = home_screen.convert()
    menu.blit(menu_image, (0, 0))

    run = True
    while run:
        if quit_game == True:
            break
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): #to quit the programm from the menu
                    run = False
            if event.type == KEYDOWN:
                if event.key == K_RETURN: #launches the game
                    run = False
                    game(map1)
                if event.key == K_TAB: #displays controls
                    display_controls = True
            if event.type == KEYUP and event.key == K_TAB:
                display_controls = False
        if run:
            if display_controls:
                menu.blit(controls.convert(), (0, 0))
            else:
                menu.blit(menu_image, (0, 0))
            pygame.display.flip() #displays the frame at the end of loop, after checking all eventual entries from the player
        continue

def game_loop(my_map, mc):
    """function that displays the game and handles the behaviour of the game,

    depending on the player entries

    """ 
    global quit_game
    diplay_list = False
    run = True
    while run:
        pygame.time.Clock().tick(30)
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): #to quit the programm from the game
                    run = False
                    quit_game = True
                    break
            if event.type == KEYDOWN: #to return to the menu
                if event.key == K_m:
                    run = False
                    menu()
                    break
                if event.key == K_TAB: #to display the item list
                    diplay_list = True
                else:
                    mc.move_MC(event.key, my_map) #calls the movement fonction of the character
            if event.type == KEYUP:
                if event.key == K_TAB:
                    diplay_list = False
        if run:
            my_map.disply_map()
            mc.display_MC(my_map)
            if diplay_list:
                mc.display_list(my_map)
            pygame.display.flip()
        if mc.win or mc.loose: #if the game is finished, calls
            run = False
            my_map.display_end(mc)
            menu()
        continue

def game(chosen_map):
    """function that initializes the map and the character, then calls the game loop"""
    my_map = RunningMap()
    my_map.load_map(chosen_map)
    my_map.place_items()
    my_map.place_guardian()
    mc = CharacterMC()
    game_loop(my_map, mc)

if __name__ == "__main__":
    menu()
