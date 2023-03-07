import logging
import yaml
import os.path
import unittest

#path = os.path.join(os.path.dirname(__file__), os.pardir,"player_options.yaml")
path = os.path.join(os.path.dirname(__file__), os.pardir)
logging.basicConfig(level=logging.DEBUG, format = '[%(asctime)s:%(levelname)s:%(name)s]: %(message)s')

def test_player_options():
    file = os.path.join(path, "player_options.yaml")
    with open(file) as f:
        logging.info("Opening file: " + file)
        options = yaml.safe_load(f)

        assert options["race"]["human"]["name"] == "Human"

        print(options["class"]["mage"]["multipliers"])

class TestPlayerOptions(unittest.TestCase):
    def test_human_name(self):
        expected = "Human"
        file = os.path.join(path, "player_options.yaml")
        with open(file) as f:
            logging.info("Opening file: " + file)
            options = yaml.safe_load(f)

            self.assertEqual(options["race"]["human"]["name"], expected)

    

if __name__ == "__main__":
    unittest.main()
