"""
Since the base game is quite long, use this to get it.
"""


def get_game_code(initialize_game: str, formatted_code: str):
    
    return """from game_library import MyGame
import arcade


def main():
    {}
    window.setup()
    arcade.run()


def user_setup(window):
{}

if __name__ == "__main__":
    main()

""".format(initialize_game, formatted_code)
