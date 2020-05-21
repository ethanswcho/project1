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

    # List of generated code from user inputs
    code = []

    code.append(program.arena.evaluate())
    for ms in program.make_statements:
        code.append(ms.evaluate())

    #main = build_main(code)
    
    main = """"""
    for c in code:
        main = main + c + "\n"

    #build_gamefile(main)

    # Check if gamefile exists first. If it does, delete it.
    if (os.path.exists(game_dir)):
        print("YES!")
        os.remove(game_dir)

    # Initialize gamefile in specified directory above, and write base game
    game_file = open(game_dir, "w")
    game_file.write(get_base_game(main))  
    game_file.close()