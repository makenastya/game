import pygame



class Hero():
    def __init__(self):
        self._health = 3
        self._attack = 20

    def attack(self, target):
        target._health -= self._attack
        print('some text')

    def is_alive(self):
        return self._health > 0
    
    
        


class health_upper():

    _points = None
    
    def add_health(self, target):
        target._health += self._points
        hero_answer = None
        game_answer = None
        return hero_answer, game_answer
    
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

