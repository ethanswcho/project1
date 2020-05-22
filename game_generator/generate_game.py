"""
input: PROGRAM object
output: game.py
"""

import os
from astNodes.PROGRAM import PROGRAM
from .get_game_code import get_game_code

game_dir = "game.py"


def generate_game(program: PROGRAM):

    # Code required to initialize the game (and arena)
    initialize_game = program.arena.evaluate()

    # List of code to be used after the game has been generated
    other_code = []

    for ms in program.make_statements:
        other_code.append(ms.evaluate())
    
    # Format the list of codes in other_code to fit python syntax
    formatted_code = """"""
    for c in other_code:
        formatted_code = formatted_code + c + "\n"

    #build_gamefile(main)

    # Check if gamefile exists first. If it does, delete it.
    if os.path.exists(game_dir):
        print("YES!")
        os.remove(game_dir)

    # Initialize gamefile in specified directory above, and write base game
    with open(game_dir, "w") as game_file:
        game_file.write(get_game_code(initialize_game, formatted_code))
