import logging
import yaml
import os.path

path = os.path.join(os.path.dirname(__file__), os.pardir,"player_options.yaml")
logging.basicConfig(level=logging.DEBUG, format = '[%(asctime)s:%(levelname)s:%(name)s]: %(message)s')

with open(path) as f:
    logging.info("Opening file: " + path)
    options = yaml.safe_load(f)

    print(options["race"])