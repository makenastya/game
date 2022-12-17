import time
import pygame
from enemies import *
from player import *
import random

def game_tournament(hero, enemy_list):
    pygame.init()

    running = True

    screen = pygame.display.set_mode((500, 500))
    player = Player()
    enemies = []
    counter = 0
    cur = 0
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        pressed_keys = pygame.key.get_pressed()
        if counter > 500 and cur < len(enemy_list):
            en = enemy_list[cur]
            if en == 'first':
                x = First()
            if en == 'second':
                x = Second()
            if en == 'third':
                x = Third()
            enemies.append(x)
            cur += 1
            counter = 0

        for x in enemies:
            x.move()
            screen.blit(x.surf, x.rect)

        player.update(pressed_keys)
        screen.blit(player.surf, player.rect)
        pygame.display.flip()
        screen.fill((0, 0, 0))
        counter += 1


def start_game():
    try:
        print('Добро пожаловать в игру про учебные долги!')
        print('Введите желаемый уровень: \n 1 уровень - вы на бт \n 2 уровень - все еще бт, но вы взяли себе вычматы \n 3 уровень - поздравляем, вы пмф')
        level = 1
        enemy_list = generate_enemy_list(level)
        hero = Player()
        print('У вас горит', len(enemy_list), 'дедлайнов!')
        game_tournament(hero, enemy_list)
    except EOFError:
        print('Поток ввода закончился. Извините, принимать ответы более невозможно.')