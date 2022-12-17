import pygame
class Player(pygame.sprite.Sprite):
    SPEED = 1
    SIZE = 30

    def __init__(self):
        self._health = 3
        self._attack = 20
        super(Player, self).__init__()
        self.surf = pygame.Surface((Player.SIZE, Player.SIZE))
        self.surf.fill((255, 255, 255))  # Change appearance
        self.rect = self.surf.get_rect(center=(
            SCREEN_WIDTH,
            SCREEN_HEIGHT
        ))
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



class health_upper():
    _quantity = None
    _points = None
    SPEED = 1
    SIZE = 1

    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((50, 50))
        self.surf.fill((255, 255, 0))  # Change appearance
        self.rect = self.surf.get_rect(center=(random.randint(0, SCREEN_WIDTH), 0))

    def move(self):
        self.rect.move_ip(0, Arrear.SPEED)
    
    def add_health(self, target):
        target._health += self._points
        hero_answer = None
        game_answer = None
        return hero_answer, game_answer

    def if_aviable(self):
        return self._quantity > 0 

    
class Coffee(health_upper):

    def __init__(self):
        self._points = 1
        self._name = 'Кружка кофе'

    def add_health(self, target):
        super().add_health()
        hero_answer = 'some text'
        game_answer = 'Физтех выпил кофе. Здоровье повышено'

    

class Annoy_neighbour(health_upper):

    def __init__(self):
        self._points = 0.5
        self._name = 'Поныть соседу'

    def add_health(self, target):
        super().add_health()
        hero_answer = 'some text'
        game_answer = 'Физтех успешно поныл соседу. Здоровье повышено.'

