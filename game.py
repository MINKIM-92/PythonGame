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
playerX_change = 0



def player(x,y):
    # Draw the player (Blit) first one image, second one is coordinates
    screen.blit(playerImg, (x,y))



# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue .
    # orders are always matters.
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystorke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #draw underneath the screen
    # 5 = 5 + 0.1
    playerX += playerX_change
    player(playerX, playerY)
    pygame.display.update()

# Change caption and logo.

