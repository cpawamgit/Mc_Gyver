import pygame
from pygame.locals import *

pygame.init()

windows = pygame.display.set_mode((640, 480))
background = pygame.image.load("background.jpg").convert()
# character = pygame.image.load("perso.png").convert_alpha()
# character_position = character.get_rect()
background_position = background.get_rect()
windows.blit(background, (150, 150))
# windows.blit(character, (120, 120))
pygame.display.flip()
print(background_position)
running = 1
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = 0
        if event.type == KEYDOWN and event.key == K_SPACE:
	        print("Espace")
        if event.type == KEYDOWN and event.key == K_DOWN:
            print(background_position)
            background_position.move(200, 200)
            windows.blit(background, background_position)
            pygame.display.flip()

    