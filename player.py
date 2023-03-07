from character import Character, CharacterEvent
import random
import yaml
import os

class Player(Character):
    def __init__(self):
        DEFAULT_VALS = {"strength": 1, "endurance": 1, "agility": 1, "wisdom": 1, "ingelligence": 1}

        self.name = ""
        self.race = None
        self.character_class = None
        self.attributes = DEFAULT_VALS
        self.multipliers = DEFAULT_VALS
        self.health = None
        self.max_health = None
        self.mana = None
        self.max_mana = None

        self.OnDeath = CharacterEvent()

    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nClass: {self.character_class}"

    def create(self):
        self.name = input("Enter Name: ")
        print_races()
        parse_race(input("Choose Race: "), self)
        print_classes()
        parse_character_class(input("Choose Class: "), self)


    def attack_action(self, target: Character):
        attack_power = self.attributes["strength"] + (random.randrange(1, 4) * self.multipliers["strength"])
        target.calculate_damage(attack_power)

    def death(self):
        self.OnDeath()

    def death_subscribe(self, obj_method):
        self.OnDeath += obj_method

    def death_unsubscribe(self, obj_method):
        self.OnDeath -= obj_method
        

def parse_race(txt: str, player: Player):
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        while not (txt in options["race"]):
            txt = input("Oops, that's not a valid race, try again: ")
        
        player.race = options["race"][txt]["name"]
        player.attributes = options["race"][txt]["attributes"]

def parse_character_class(txt: str, player: Player):
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        while not (txt in options["class"]):
            txt = input("Oops, that's not a valid class, try again: ")

        player.character_class = options["class"][txt]["name"]
        player.multipliers = options["class"][txt]["multipliers"]

def print_races():
    os.system("cls")
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        for _, race_val in options["race"].items():
            txt_name = race_val["name"]
            txt_attr = race_val["attributes"]
            print(f'{txt_name} - {txt_attr}')

def print_classes():
    os.system("cls")
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        for _, cls_val in options["class"].items():
            txt_name = cls_val["name"]
            txt_mult = cls_val["multipliers"]
            print(f'{txt_name} - Bonus(*): {txt_mult}')