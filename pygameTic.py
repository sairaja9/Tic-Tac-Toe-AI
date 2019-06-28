import pygame

# Initialization - the window color and caption is set here
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe by Sai and Rishabh")

# Colors - Used to change text, line, and background colors
JET = [33,34,33]
SKYBLUE = [169,206,244]
MIDNIGHTBLUE = [27,59,111]
CORALRED = [255, 62, 65]
IVORY = [193,193,193]

screen.fill(JET)

# Lines - Draws the Tic Tac Toe Game Board (hashtag shape)
pygame.draw.line(screen, IVORY, (225, 525), (225, 75), 3)
pygame.draw.line(screen, IVORY, (375, 525), (375, 75), 3)
pygame.draw.line(screen, IVORY, (75, 225), (525, 225), 3)
pygame.draw.line(screen, IVORY, (75, 375), (525, 375), 3)

# The screen color and display refreshing is set here
pygame.display.flip()


class player(object):
    def __init__(self): 
        pass

    def checkClick(self, position):

        # Position Ranges - Using these ranges, we can check which box/board position was clicked (done in checkClick function)
        rows = [(75, 225), (225, 375), (375, 525)]

        if self.pos[1] > rows[0][0] and self.pos[1] < rows[0][1]:
            if self.pos[0] > rows[0][0] and self.pos[0] < rows[0][1]:
                self.playerPosition = 'bottomLeft'
            elif self.pos[0] > rows[1][0] and self.pos[0] < rows[1][1]:
                self.playerPosition = 'bottomCenter'
            elif self.pos[0] > rows[2][0] and self.pos[0] < rows[2][1]:
                self.playerPosition = 'bottomRight'

        if self.pos[1] > rows[1][0] and self.pos[1] < rows[1][1]:
            if self.pos[0] > rows[0][0] and self.pos[0] < rows[0][1]:
                self.playerPosition = 'middleLeft'
            elif self.pos[0] > rows[1][0] and self.pos[0] < rows[1][1]:
                self.playerPosition = 'middleCenter'
            elif self.pos[0] > rows[2][0] and self.pos[0] < rows[2][1]:
                self.playerPosition = 'middleRight'

        if self.pos[1] > rows[2][0] and self.pos[1] < rows[2][1]:
            if self.pos[0] > rows[0][0] and self.pos[0] < rows[0][1]:
                self.playerPosition = 'topLeft'
            elif self.pos[0] > rows[1][0] and self.pos[0] < rows[1][1]:
                self.playerPosition = 'topCenter'
            elif self.pos[0] > rows[2][0] and self.pos[0] < rows[2][1]:
                self.playerPosition = 'topRight'


        if self.playerPosition == 'topLeft':
            screen.blit(IconPlayer, (130, 450))
        elif self.playerPosition == 'topCenter':
            screen.blit(IconPlayer, (280, 450))
        elif self.playerPosition == 'topRight':
            screen.blit(IconPlayer, (430, 450))

        if self.playerPosition == 'middleLeft':
            screen.blit(IconPlayer, (130, 300))
        elif self.playerPosition == 'middleCenter':
            screen.blit(IconPlayer, (280, 300))
        elif self.playerPosition == 'middleRight':
            screen.blit(IconPlayer, (430, 300))

        if self.playerPosition == 'bottomLeft':
            screen.blit(IconPlayer, (130, 150))
        elif self.playerPosition == 'bottomCenter':
            screen.blit(IconPlayer, (280,150))
        elif self.playerPosition == 'bottomRight':
            screen.blit(IconPlayer, (430, 150))

playerX = player()
playerO = player()
currentPlayer = playerX
run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONUP:
            currentPlayer.pos = pygame.mouse.get_pos()
            currentPlayer.checkClick(currentPlayer.pos)
            pygame.display.flip()

    if currentPlayer == playerX:
        IconPlayer = pygame.image.load('IconPlayerO.png')
        currentPlayer = playerO
    elif currentPlayer == playerO:
        IconPlayer = pygame.image.load('IconPlayerX.png')
        currentPlayer = playerX