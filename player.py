import yaml
import os

class Player:
    def __init__(self):
        self.name = ""
        self.race = None
        self.character_class = None
        self.attributes = {}
        self.multipliers = {}
        self.health = None
        self.max_health = None
        self.mana = None
        self.max_mana = None

    def __str__(self):
        return f"Name: {self.name}\nRace: {self.race}\nClass: {self.character_class}"

    def create(self):
        self.name = input("Enter Name: ")
        print_races()
        self.race = parse_race(input("Choose Race: "))

    def attack_action(self, target):
        attack_power = self.strength * self.multipliers

def parse_race(txt: str):
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        while not (txt in options["race"]):
            txt = input("Oops, that's not a valid race, try again: ")

        return options["race"][txt]["name"]

def parse_character_class(txt: str):
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        while not (txt in options["class"]):
            txt = input("Oops, that's not a valid class, try again: ")

        return options["class"][txt]["name"]

def print_races():
    os.system("cls")
    with open("player_options.yaml") as f:
        options = yaml.safe_load(f)

        for race, race_val in options["race"].items():
            txt_name = race_val["name"]
            txt_attr = race_val["attributes"]
            print(f'{txt_name} - {txt_attr}')