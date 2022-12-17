import time

from enemies import *
from hero import *

def game_tournament(hero, enemy_list):
    pygame.init()

    running = True

    screen = pygame.display.set_mode((500, 500))

    player = Player()
    enemies = []

    counter = 0

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pressed_keys = pygame.key.get_pressed()

        for en in enemy_list:
            if enemy_list[cur] == 'first':
                x = First()
            if enemy_list[cur] == 'second':
                x = Second()
            if enemy_list[cur] == 'third':
                x = Third()
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
        print('Как вас звать? (или вы сами приходите?) ', end = '')
        hero = Hero(input())
        print('Введите желаемый уровень: \n 1 уровень - вы на бт \n 2 уровень - все еще бт, но вы взяли себе вычматы \n 3 уровень - поздравляем, вы пмф')

        level = int(input())
        enemy_list = generate_enemy_list(level)

        print('У вас горит', enemy_list.size(), 'дедлайнов!')
        game_tournament(hero, enemy_list)
