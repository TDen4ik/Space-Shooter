import math

import pygame
import time
import pygame.mixer
pygame.mixer.init()
from pygame.locals import *

BACKGROUND_IMAGE = pygame.transform.scale(
    pygame.image.load("background.jpg"), (800, 600)
)
PLAYER_IMAGE = pygame.transform.scale(
    pygame.image.load("player2.png"), (60, 60)
)

ENEMY_IMAGE = pygame.transform.scale(
    pygame.image.load("enemy.png"), (50, 50)
)

SHOT_IMAGE = pygame.transform.scale(
    pygame.image.load("shot.jpg"), (20, 20)
)

shoot = pygame.mixer.Sound("shot_sound.mp3")

bacraund_muzic = pygame.mixer.Sound("music.mp3")
pygame.init()
x = 800
y = 600
white = (23, 11, 143)
black = (43, 0, 1)
red = (255, 88, 0)

dis = pygame.display.set_mode((x, y))
pygame.display.set_caption('Space Shooter')
bacraund_muzic.play()
clock = pygame.time.Clock()

game_over = False
player = pygame.rect.Rect(400, 530, 50, 50)
enemies = []

start_time = time.time()

for j in range(1, 4):
    for i in range(7):
        enemies.append(pygame.rect.Rect(i * 100 + 80, 75 * j, 50, 50))

bullets = []

while not game_over:
    dis.blit(BACKGROUND_IMAGE, (0, 0))
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        if event.type == KEYDOWN:
            if event.key == K_SPACE and len(bullets) < 6:
                bullets.append(pygame.rect.Rect(player.x + player.width // 2, player.y, 5, 10))
                shoot.play()

    pressed = pygame.key.get_pressed()

    for enemy in enemies:
        dis.blit(ENEMY_IMAGE, (enemy.x, enemy.y))

    for bullet in bullets:
        pygame.draw.rect(dis, (22,180,247), bullet)

    for enemy in enemies:
        if math.floor(start_time - current_time) % 5 == 0:
            enemy.y += 1
        if enemy.colliderect(player):
            print("U LOSE!!!!")

            game_over = True

    for bullet in bullets:
        if bullet.y < 0:
            bullets.remove(bullet)
        else:
            bullet.y -= 3

        for enemy in enemies:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)

    if pressed[K_a] and player.x > 0:
        player.x -= 5
    if pressed[K_d] and player.x < 750:
        player.x += 5

    dis.blit(PLAYER_IMAGE, (player.x, player.y))

    if not enemies:
        print("U WIN!!!!!")
        game_over = True
    pygame.display.update()

    clock.tick(30)

pygame.quit()
quit()
