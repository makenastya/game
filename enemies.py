class Enemy():
    _health = None
    _attack = None
    _time = None

    def attack(self, target):
        target._health -= self._attack

    def is_alive(self):
        return self._health > 0

    def generate_random_enemy():
        RandomEnemyType = choice(enemy_types)
        enemy = RandomEnemyType()
        return enemy

    def generate_dragon_list(enemy_number):
        enemy_list = [generate_random_enemy() for i in range(enemy_number)]
        return enemy_list

enemy_types=[fizra, proga, biochem]

class Fizra(Enemy):
    def __init__(self):
        self._health = 50
        self._time = 100
        self._type = 'Физра'

class Proga(Enemy):
    def __init__(self):
        self._health = 100
        self._time = 80
        self._type = 'Прога'

class Biochem(Enemy):
    def __init__(self):
        self._health = 200
        self._time = 50
        self._type = 'БиОхИмИя'

