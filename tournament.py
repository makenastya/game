import time
import pygame
from enemies import *
from player import *
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700

def game_tournament(level, screen):
    running = True
    hero = Player()
    enemy_list = generate_enemy_list(level)
    enemies = []
    counter = 0
    cur = 0
    fl = 0
    while running:
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
                    print(hero._health)
                enemies.remove(x)

        for x in enemies:
            if not x.on_screen() and x._type != 'health_upper':
                x.attack(hero)
                print(hero._health)
                enemies.remove(x)

        hero.update(pressed_keys)
        screen.blit(hero.surf, hero.rect)
        pygame.display.flip()
        screen.fill((135, 206, 250))
        counter += 1
        time.sleep(0.001)

        if hero._health <= 0:
            print('You lose')
            running = False
        if len(enemies) == 0 and fl == 1:
            print('You win')
            running = False

def start_game():
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        print('Добро пожаловать в игру про учебные долги!')
        print('Введите желаемый уровень: \n 1 уровень - вы на бт \n 2 уровень - все еще бт, но вы взяли себе вычматы \n 3 уровень - поздравляем, вы пмф')
        level = 2
        enemy_list = generate_enemy_list(level)
        print('У вас горит', len(enemy_list), 'дедлайнов!')
        game_tournament(level, screen)
    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')