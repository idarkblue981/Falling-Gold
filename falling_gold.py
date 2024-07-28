from math import sqrt
from random import randint
from pygame import mixer
import pygame

pygame.init()


# Screen and background
screen = pygame.display.set_mode((800, 600))
background_picture = pygame.image.load("./art/background.png")


# Window title and icon
pygame.display.set_caption("Falling Gold")
window_icon = pygame.image.load("./art/window-icon.png")
pygame.display.set_icon(window_icon)


# Music and sound effects
mixer.music.load("./music and sound effects/music.wav")
mixer.music.play(-1)
game_over_sound = mixer.Sound("./music and sound effects/game-over-sound.wav")
coin_sound = mixer.Sound("./music and sound effects/coin-sound.wav")


# Chest
chest = pygame.image.load("./art/chest.png")
chestPosX = 400
chestPosY = 410
chestPosX_change = 0


# Coin and ingot
coin = pygame.image.load("./art/coin.png")
coinPosX = randint(0, 736)
coinPosY = 0
coinPosY_change = 10

ingot = pygame.image.load("./art/ingot.png")
ingotPosX = randint(0, 736)
ingotPosY = 0
ingotPosY_change = 15


# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

def show_score(x, y):
    score_display = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_display, (x, y))


# Distance
def distance(x_two, x_one, y_two, y_one):
    distance = sqrt(((x_two - x_one) ** 2) + ((y_two - y_one) ** 2))
    return distance


# Reset coin and ingot positions
def reset_positions():
    global coinPosX, coinPosY, ingotPosX, ingotPosY
    coinPosX = randint(0, 736)
    coinPosY = 0
    ingotPosX = randint(0, 736)
    ingotPosY = 0


# Main loop
running = True
while running:

    screen.blit(background_picture, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_LEFT:
                chestPosX_change = -25
            elif event.key == pygame.K_RIGHT:
                chestPosX_change = 25
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                chestPosX_change = 0


    # Chest boundaries
    chestPosX += chestPosX_change
    if chestPosX < 0:
        chestPosX = 0
    elif chestPosX > 672:
        chestPosX = 672


    # Coin and ingot movement
    coinPosY += coinPosY_change
    ingotPosY += ingotPosY_change


    # Check if coin or ingot reached the bottom of the screen
    if coinPosY > 600 or ingotPosY > 600:
        game_over_sound.play()
        score = 0
        reset_positions()


    # Check for collisions with chest
    if distance(chestPosX + 64, coinPosX + 32, chestPosY, coinPosY) < 64:
        score += 1
        coinPosY = 0
        coinPosX = randint(0, 736)
        coin_sound.play()
    if distance(chestPosX + 64, ingotPosX + 32, chestPosY, ingotPosY) < 64:
        score += 5
        ingotPosY = 0
        ingotPosX = randint(0, 736)
        coin_sound.play()


    # Draw
    screen.blit(coin, (coinPosX, coinPosY))
    screen.blit(ingot, (ingotPosX, ingotPosY))
    screen.blit(chest, (chestPosX, chestPosY))


    # Score
    show_score(10, 10)

    pygame.display.update()