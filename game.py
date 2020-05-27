import pygame
import random
import math



#Creating the first window

# Intialize the pygame.
pygame.init()


# cretae the screen - 800 width 600 height.
screen = pygame.display.set_mode((800,600))

#add background

background = pygame.image.load('33.png')

#Title and Icon

pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('icon2.png')
pygame.display.set_icon(icon)


# Create player
playerImg = pygame.image.load('icon4.png')
playerX = 320
playerY = 480
playerX_change = 0

#Create enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('bug2.png'))

    enemyX.append(random.randint(0,800))
    enemyY.append(random.randint(50,150))

    enemyX_change.append(2)
    enemyY_change.append(40)

#Create bullet


# Ready - means you can't see the bullet on the screen
# Fire - The bullet is currently moving

bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480

bulletX_change = 0
bulletY_change = 15
bullet_state = "ready"

score = 0

def player(x,y):
    # Draw the player (Blit) first one image, second one is coordinates
    screen.blit(playerImg, (x,y))

def enemy(x,y,i):
    # Draw the player (Blit) first one image, second one is coordinates
     screen.blit(enemyImg[i], (x,y))

def fire_bullet(x,y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg,(x+ 47 ,y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distacnce = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY,2)))

    if distacnce < 27:
        return True
    else:
        return False



# Game Loop
running = True
while running:

    # RGB - Red, Green, Blue .
    # orders are always matters.
    screen.fill((0, 0, 0))
    #Background Image

    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if keystorke is pressed check wheter its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready" :
                 bulletX = playerX
                 fire_bullet(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    #draw underneath the screen
    # 5 = 5 + 0.1
    playerX += playerX_change


    # Checking for boundaries of spaceship so it doesn't go out of bounds
    if playerX <= 0:
        playerX = 0
    elif playerX >= 686:
        playerX = 686

    # Enemy movements
    for i in range(num_of_enemies):

        enemyX[i] += enemyX_change[i]

        if enemyX[i] <= 0:
            enemyX_change[i] = 2
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 730:
            enemyX_change[i] = -2
            enemyY[i] += enemyY_change[i]

        # collision

        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 460
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 800)
            enemyY[i] = random.randint(50, 150)

        enemy(enemyX[i],enemyY[i],i)

    # Bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire" :
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change

    # Collision


        print(score)

    player(playerX, playerY)
    pygame.display.update()

# Change caption and logo.

