import time
import pygame
from enemies import *
from player import *
from game_over import *
from win import *
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

def game_tournament(level, screen):
    running = True
    hero = Player()
    enemy_list = generate_enemy_list(level)
    f1 = pygame.font.Font(None, 30)
    screen.fill((61, 245, 190))
    image = pygame.image.load("heart.png")
    image = pygame.transform.scale(image, (50, 35))
    image.set_colorkey((255, 255, 255))
    string = pygame.Rect(0, 0, SCREEN_WIDTH, 0).inflate(1200, 100)

    enemies = []
    counter = 0
    cur = 0
    fl = 0
    cf = 0
    at = 0
    while running:
        pygame.draw.rect(screen, (0, 0, 0), string)
        screen.blit(image, (20, 10))
        heart = f1.render(str(hero._health), True, (255, 255, 255))
        screen.blit(heart, (70, 20))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        if counter > 350 and cur < len(enemy_list):
            fl = 1
            en = enemy_list[cur]
            if en == 'first':
                x = First()
            if en == 'second':
                x = Second()
            if en == 'third':
                x = Third()
            if en == 'coffee':
                x = Coffee()
            if en == 'annoy_neighbour':
                x = Annoy_neighbour()
            enemies.append(x)
            cur += 1
            counter = 0

        for x in enemies:
            x.move()
            screen.blit(x.surf, x.rect)

        for x in enemies:
            if pygame.sprite.collide_rect(hero, x):
                if x._type == 'health_upper':
                    x.add_health(hero)
                    cf = 1
                    message = x._message
                    print(hero._health)
                enemies.remove(x)

        if cf > 0:
            if cf > 200 or at > 0:
                cf = 0
            else:
                text = f1.render(message, True, (255, 255, 255))
                screen.blit(text, (500, 10))
                cf += 1
        for x in enemies:
            if not x.on_screen() and x._type != 'health_upper':
                x.attack(hero)
                at = 1
                uron = x._attack
                enemies.remove(x)
        if at > 0:
            if at > 200 or cf > 0:
                at = 0
            else:
                text = f1.render(f'Вы пропустили дедлайн, минус {uron} здоровья', True, (255, 255, 255))
                screen.blit(text, (500, 10))
                at += 1
        hero.update(pressed_keys)
        screen.blit(hero.surf, hero.rect)
        pygame.display.flip()
        counter += 1
        time.sleep(0.001)
        screen.fill((61, 245, 190))
        if hero._health <= 0:
            game_over()
            running = False
        if len(enemies) == 0 and fl == 1:
            win()
            running = False

