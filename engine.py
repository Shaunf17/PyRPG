from player import Player

class Game:
    def __init__(self):
        self.state = GameState()
        self.world = World()
        self.player = Player()
        self.parser = Parser()

    def run(self):
        print("Welcome to the game!")
        while True:
            command = input("> ")
            action = self.parser.parse(command)
            if action:
                action.execute(self)

class GameState:
    def __init__(self):
        self.location = None
        self.inventory = []

class World:
    def __init__(self):
        self.map = Map()

class Map:
    def __init__(self):
        self.locations = []

class Parser:
    def parse(self, command):
        match command:
            case "n" | "s" | "e" | "w":
                # Move in a direction
                return MoveAction(command)
            case "look":
                # Look around the current location
                return LookAction()
            case "inventory":
                # Check the player's inventory
                return InventoryAction()
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

class LookAction(Action):
    def execute(self, game):
        # Display information about the current location
        pass

class InventoryAction(Action):
    def execute(self, game):
        # Display the player's inventory
        pass

class HelpAction(Action):
    def execute(self, game):
        # Display a list of available commands
        print("ayy, stfu")

if __name__ == "__main__":
    game = Game()
    game.run()
