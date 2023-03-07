class Character:
    def __init__(self,
                 name = "",
                 race = None,
                 character_class = None,
                 attributes = {},
                 multiplers ={},
                 max_health = None,
                 max_mana = None
                 ):
        
        self.name = name
        self.race = race
        self.character_class = character_class
        self.attributes = attributes
        self.multipliers = multiplers
        self.health = max_health
        self.max_health = max_health
        self.mana = max_mana
        self.max_mana = max_mana

    def calculate_damage(self, attack_damage):
        self.health -= attack_damage
        print(f'{self.name} took {attack_damage} damage!')
        print(f'{self.name} health: {self.health}')
        if self.health <= 0:
            self.death()

    def death(self):
        print(f'{self.name} has died')

class CharacterEvent(object):
    def __init__(self):
        self._eventhandlers = []

    def __iadd__(self, handler):
        self._eventhandlers.append(handler)
        return self
    
    def __isub__(self, handler):
        self._eventhandlers.remove(handler)
        return self
    
    def __call__(self, *args, **kwargs):
        for eventhandler in self._eventhandlers:
            eventhandler(*args, **kwargs)