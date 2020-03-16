# import pygame
# from pygame.locals import *

# from constants import *
# from classes import RunningMap
# from classes import CharacterDK

# pygame.init()
# quit_game = False
# sound = pygame.mixer.Sound("GramatikOGG")
# menu = pygame.display.set_mode((450, 450))
# menu_image = home_screen.convert()
# menu.blit(menu_image, (0, 0))
# sound.set_volume(0.5)

# run = True
# is_playing = False
# while run:
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_SPACE:
#                 if is_playing == False:
#                     is_playing = True
#                     sound.play()
#                 else:
#                     pygame.mixer.unpause()
#             if event.key == K_RETURN:
#                 is_playing = False
#         if event.type == KEYUP:
#             if event.key == K_SPACE:
#                 pygame.mixer.pause()
#     pygame.display.flip()
#     continue

import random

x = random.randrange(0, 61, 30)
print(x)