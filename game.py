from game_library import MyGame
from objects.mutable_block import MutableBlock
import arcade


def main():
    window = MyGame(setup_func=user_setup, width=12, height=12, title="Game")
    window.setup()
    arcade.run()


def user_setup(window):
    g1 = MutableBlock(window, (11, 1), is_goal=True)
    g2 = MutableBlock(window, (1, 4), is_goal=True)
    b2 = MutableBlock(window, (2, 2))
    b3 = MutableBlock(window, (3, 3))
    b4 = MutableBlock(window, (4, 4))
    b5 = MutableBlock(window, (5, 5))
    b6 = MutableBlock(window, (6, 6))
    b7 = MutableBlock(window, (7, 7))


if __name__ == "__main__":
    main()

