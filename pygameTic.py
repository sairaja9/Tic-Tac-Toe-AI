import pygame
pygame.init()

screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe by Sai and Rishabh")
bg = pygame.image.load('ticgameboard2.png')

WHITE = (255,255,255)

class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
def redrawGameWindow():
    screen.fill(WHITE)
    screen.blit(bg, (0,0))

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()