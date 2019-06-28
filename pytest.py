import pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))


run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            coordinates = pygame.mouse.get_pos()
            print(coordinates)