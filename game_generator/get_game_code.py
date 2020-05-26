"""
Since the base game is quite long, use this to get it.
"""


def get_game_code(initialize_game: str, formatted_code: str):
    
    return """from game_library import MyGame
from objects.mutable_block import MutableBlock
import arcade
import pyglet


class UserGame:

    def __init__(self, window: arcade.Window):
        self.window = window
        
    def user_setup(self):
{}

def main():
    {}
    user_game = UserGame(window)
    window.setup_func = user_game.user_setup
    window.destroy_func = user_game.destroy
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

""".format(formatted_code, initialize_game)
