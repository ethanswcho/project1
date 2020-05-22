from game_library import MyGame
import arcade


def main():
    window = MyGame(setup_func=user_setup, width=12, height=12, title="Game")
    window.setup()
    arcade.run()


def user_setup(window):
    b2 = window.make_block([2, 2])
    b3 = window.make_block([3, 3])
    b4 = window.make_block([4, 4])
    b5 = window.make_block([5, 5])
    b6 = window.make_block([6, 6])
    b7 = window.make_block([7, 7])


if __name__ == "__main__":
    main()

