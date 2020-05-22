import pygame

#Creating the first window

# Intialize the pygame.
pygame.init()


# cretae the screen - 800 width 600 height.
screen = pygame.display.set_mode((800,600))


#Title and Icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon2.png')
pygame.display.set_icon(icon)


# Create player
playerImg = pygame.image.load('icon4.png')
playerX = 320
playerY = 480



def player():
    # Draw the player (Blit) first one image, second one is coordinates
    screen.blit(playerImg, (playerX,playerY))


# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue .
    # orders are always matters.
    screen.fill((0, 0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    #draw underneath the screen
    player()
    pygame.display.update()

# Change caption and logo.

