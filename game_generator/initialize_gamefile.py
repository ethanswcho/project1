"""
Initialize game with arena settings (if any)
"""

from .get_base_game import get_base_game
import os

game_dir = "game.py"

def initialize_gamefile():
    print(game_dir)

    # Check if gamefile exists first. If it does, delete it.
    if (os.path.exists(game_dir)):
        print("YES!")
        os.remove(game_dir)

    # Initialize gamefile in specified directory above, and write base game
    game_file = open(game_dir, "w")
    game_file.write(get_base_game())   
    