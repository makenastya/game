from random import choice
import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 500, 500
class Enemy(pygame.sprite.Sprite):

    _health = None
    _attack = None
    _time = None
    _start = None
    SPEED = 1
    SIZE = 1

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 0))  # Change appearance
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH), 0))

    def move(self):
        self.rect.move_ip(0, Enemy.SPEED)
    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0

    def generate_random_enemy(listt):
        RandomEnemyType = choice(listt)
        enemy = RandomEnemyType()
        return enemy

def generate_enemy_list(level):
    if level == 1:
        enemy_list = ['first' for i in range(3)]
        enemy_list += ['second' for i in range(3)]
    if level == 2:
        enemy_list = ['first' for i in range(2)]
        enemy_list += ['second' for i in range(4)]
        enemy_list.append('third')
    if level == 3:
        enemy_list = ['first' for i in range(3)]
        enemy_list += ['second' for i in range(6)]
        enemy_list.append('third')
        enemy_list.append('third')
    return enemy_list


class First(Enemy):
    def __init__(self):
        super(First, self).__init__()
        self._health = 40
        self._time = 100
        self._type = 'first'
        self._attack = 1

class Second(Enemy):
    def __init__(self):
        super(Second, self).__init__()
        self._health = 100
        self._time = 80
        self._type = 'second'
        self._attack = 1

class Third(Enemy):
    def __init__(self):
        super(Third, self).__init__()
        self._health = 200
        self._time = 50
        self._type = 'boss'
        self._attack = 2

