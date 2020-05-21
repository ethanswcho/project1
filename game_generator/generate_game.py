"""
input: PROGRAM object
output: game.py
"""

import os

from game_helpers import make_block
from astNodes.PROGRAM import PROGRAM
from .build_main import build_main
from .build_gamefile import build_gamefile

from .get_base_game import get_base_game

game_dir = "game.py"


def generate_game(program: PROGRAM):



    # Code required to initialize the game (and arena)
    initialize_game = program.arena.evaluate()

    # List of code to be used after the game has been generated
    other_code = []

    for ms in program.make_statements:
        other_code.append(ms.evaluate())

    #main = build_main(code)
    
    # Format the list of codes in other_code to fit python syntax
    formatted_code = """"""
    for c in other_code:
        formatted_code = formatted_code + c + "\n"

    #build_gamefile(main)

    # Check if gamefile exists first. If it does, delete it.
    if (os.path.exists(game_dir)):
        print("YES!")
        os.remove(game_dir)

    # Initialize gamefile in specified directory above, and write base game
    game_file = open(game_dir, "w")
    game_file.write(get_base_game(initialize_game, formatted_code))  
    game_file.close()