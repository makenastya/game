import time

from enemies import *
from hero import *


def game_tournament(hero, enemy_list):
    start = time.time()
    cur = 0
    temp = []
    for i in range(3):
        if enemy_list[cur] == 'first':
            x = First()
        if enemy_list[cur] == 'second':
            x = Second()
        if enemy_list[cur] == 'third':
            x = Third()
        x.start = time.time()
        temp.append(x)
        cur += 1
    while cur < enemy_list.size() and hero.is_alive():
        clicked_number = 0
        while temp[clicked_number].is_alive() and hero.is_alive():
            hero.attack(temp[clicked_number])
            if time.time() - temp[clicked_number].start > temp[clicked_number].time:
                temp[clicked_number].attack(hero)
                temp.remove(clicked_number)
        #if event.type == pygame.MOUSEBUTTONDOWN:
            #if #условие что нажали на кофе и оно в наличии
                #Coffee.add_health()
        if time.time() - start > 10:
            for i in range(min(3, enemy_list.size() - cur)):
                if enemy_list[cur] == 'first':
                    x = First()
                if enemy_list[cur] == 'second':
                    x = Second()
                if enemy_list[cur] == 'third':
                    x = Third()
                x.start = time.time()
                temp.append(x)
                cur += 1
            start = time.time()

def start_game():

    try:
        print('Добро пожаловать в игру про учебные долги!')
        print('Как вас звать? (или вы сами приходите?) ', end = '')
        hero = Hero(input())
        print('Введите желаемый уровень: \n 1 уровень - вы на бт \n 2 уровень - все еще бт, но вы взяли себе вычматы \n 3 уровень - поздравляем, вы пмф')

        level = int(input())
        enemy_list = generate_enemy_list(level)

        print('У вас горит', enemy_list.size(), 'дедлайнов!')
        game_tournament(hero, enemy_list)
