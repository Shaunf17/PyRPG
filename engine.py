from character import Character, CharacterEvent
from player import Player
from game_state import GameState
import os

class Game:
    def __init__(self):
        self.state = GameState()
        self.world = World()
        self.player = Player()
        self.parser = Parser()

        self.player.death_subscribe(game_over)

    def run(self):
        os.system("cls")
        print("Welcome to the game!")

        self.player.create()
        print(self.player)

        while True:
            command = input("> ")
            action = self.parser.parse(command)
            if action:
                action.execute(self)

def game_over():
    os.system("cls")
    print("GAME OVER")
    exit()

class World:
    def __init__(self):
        self.map = Map()

class Map:
    def __init__(self):
        self.locations = []

class Parser:
    def parse(self, command):
        # Split arg in command and argument
        command_args = str.split(command)

        match command_args[0]:
            case "n" | "s" | "e" | "w":
                # Move in a direction
                return MoveAction(command_args)
            case "go":
                return GoAction(command_args)
            case "look":
                # Look around the current location
                return LookAction()
            case "inventory":
                # Check the player's inventory
                return InventoryAction()
            case "battle" | "fight":
                # Fight/Battle action
                return FightAction()
            case "help":
                # Display a help message
                return HelpAction()
            case _:
                # Unrecognized command
                print("I don't understand that command. Type 'help' for a list of commands.")
                return None

class Action:
    def execute(self, game):
        pass

class MoveAction(Action):
    def __init__(self, direction):
        self.direction = direction

    def execute(self, game):
        # Move the player to the new location
        pass

class GoAction(Action):
    def execture(self, game):
        # Move to specific location
        pass

class LookAction(Action):
    def execute(self, game):
        # Display information about the current location
        pass

class InventoryAction(Action):
    def execute(self, game):
        # Display the player's inventory
        pass

class FightAction(Action):
    def execute(self, game: Game):
        # TODO: implement proper method
        enemy = Character("MeeMar", "Goblin", None, {"strength": 3}, {}, 10, 10)
        print(f'You encounter {enemy.name} ({enemy.race}), what do you do?')

        while (enemy.health > 0):
            if input("> ") == "attack":
                print(f'You attack {enemy.name}')
                game.player.attack_action(enemy)
                

class HelpAction(Action):
    def execute(self, game):
        # Display a list of available commands
        print("ayy, stfu")