import pygame

# Initialization - the window color and caption is set here
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Tic Tac Toe by Sai and Rishabh")

# Colors - Used to change text, line, and background colors
JET = [44,44,43]
SKYBLUE = [169,206,244]
MIDNIGHTBLUE = [27,59,111]
CORALRED = [255, 62, 65]
IVORY = [193,193,193]

# Lines - Draws the Tic Tac Toe Game Board (hashtag shape)
pygame.draw.line(screen, IVORY, (225, 525), (225, 75), 3)
pygame.draw.line(screen, IVORY, (375, 525), (375, 75), 3)
pygame.draw.line(screen, IVORY, (75, 225), (525, 225), 3)
pygame.draw.line(screen, IVORY, (75, 375), (525, 375), 3)

# The screen color and display refreshing is set here
screen.fill(JET)
pygame.display.flip()


class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def checkClick():

        # Position Ranges - Using these ranges, we can check which box/board position was clicked (done in checkClick function)
        rows = [(self.x>75, self.x<225), (self.x>225, self.x<375), (self.x>375, self.x<525)]
        cols = [(self.y>375, self.y<525), (self.y>225, self.y<373), (self.y>75, self.y<225)]
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

        if rows[0][0] == pos[0] and rows[0][1] == pos[0]:
            if cols[0]:
                self.playerPosition = 'topLeft'
            elif cols[1]:
                self.playerPosition = 'topCenter'
            elif cols[2]:
                self.playerPosition = 'topRight'

        if rows[1]:
            if cols[0]:
                self.playerPosition = 'centerLeft'
            elif cols[1]:
                self.playerPosition = 'centerCenter'
            elif cols[2]:
                self.playerPosition = 'centerRight'

        if rows[3]:
            if cols[0]:
                self.playerPosition = 'centerLeft'
            elif cols[1]:
                self.playerPosition = 'centerCenter'
            elif cols[2]:
                self.playerPosition = 'centerRight'

    
def redrawGameWindow():
    pass

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    redrawGameWindow()