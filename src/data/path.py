from pathlib import Path
from os.path import join, dirname, realpath
from sys import argv

base_path = dirname(realpath(argv[0]))

user_path = Path.home()

main_path = join(user_path, 'AppData', 'LocalLow', 'EatRawPM')