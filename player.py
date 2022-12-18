import pygame
import random

SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 700
from pygame import (
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    RLEACCEL
)
class Player(pygame.sprite.Sprite):
    SPEED = 3
    SIZE = 30
    def __init__(self):
        super(Player, self).__init__()
        self._health = 3
        self._attack = 20
        pic = pygame.image.load("hero.png")
        pic = pygame.transform.scale(pic, (100, 100))
        self.surf = pic
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH, SCREEN_HEIGHT))
    def attack(self, target):
        target._health -= self._attack
        print('some text')

    def is_alive(self):
        return self._health > 0
    def update(self, keys):
        if keys[K_LEFT]:
            self.rect.move_ip(-Player.SPEED, 0)
        elif keys[K_RIGHT]:
            self.rect.move_ip(Player.SPEED, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

        if self.rect.top <= 0:
            self.rect.top = 0

        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT



class health_upper(pygame.sprite.Sprite):
    _quantity = None
    _points = None
    SPEED = 1
    SIZE = 1

    def __init__(self):
        super(health_upper, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH), 0))

    def move(self):
        self.rect.move_ip(0, health_upper.SPEED)
    def on_screen(self):
        return self.rect.top < SCREEN_HEIGHT
    
    def add_health(self, target):
        target._health += self._points

    def if_aviable(self):
        return self._quantity > 0 

    
class Coffee(health_upper):

    def __init__(self):
        super(Coffee, self).__init__()
        self.surf.fill((130, 93, 20))  # Change appearance
        self._points = 1
        self._name = 'Кружка кофе'
        self._message = 'Физтех выпил кофе. Здоровье повышено'
        self._type = 'health_upper'

    def add_health(self, target):
        super().add_health(target)
        hero_answer = 'some text'
        game_answer = 'Физтех выпил кофе. Здоровье повышено'
        print('Физтех выпил кофе. Здоровье повышено')
    

class Annoy_neighbour(health_upper):

    def __init__(self):
        super(Annoy_neighbour, self).__init__()
        self.surf.fill((222,247, 54))
        self._points = 0.5
        self._name = 'Поныть соседу'
        self._message = 'Физтех успешно поныл соседу. Здоровье повышено.'
        self._type = 'health_upper'

    def add_health(self, target):
        super().add_health(target)
        hero_answer = 'some text'
        game_answer = 'Физтех успешно поныл соседу. Здоровье повышено.'
        print('Физтех успешно поныл соседу. Здоровье повышено.')
