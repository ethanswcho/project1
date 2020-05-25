from game_library import MyGame
from objects.mutable_block import MutableBlock
import arcade
import pyglet


class UserGame:

    def __init__(self, window: arcade.Window):
        self.window = window
        
    def user_setup(self):
        self.g1 = MutableBlock(self.window, (11, 1), is_goal=True)
        self.g2 = MutableBlock(self.window, (1, 4), is_goal=True)
        self.b2 = MutableBlock(self.window, (2, 2))
        self.b3 = MutableBlock(self.window, (3, 3))
        self.b4 = MutableBlock(self.window, (4, 4))
        self.b5 = MutableBlock(self.window, (5, 5))
        self.b6 = MutableBlock(self.window, (6, 6))
        self.b7 = MutableBlock(self.window, (7, 7))
        arcade.schedule(self.loop0, 2.0)
        arcade.schedule(self.loop1, 6.0)
        arcade.schedule(self.loop2, 3.0)

    def loop0(self, dt):
        pyglet.clock.schedule_once(lambda dt: setattr(self, 'b8', MutableBlock(self.window, (4, 7))), 0)
        pyglet.clock.schedule_once(lambda dt: self.b8.kill(), 1.0)


    def loop1(self, dt):
        pyglet.clock.schedule_once(self.b5.set_block_xpos, 0, 8)
        pyglet.clock.schedule_once(self.b5.set_block_ypos, 1.0, 8)
        pyglet.clock.schedule_once(self.b5.change_block_xpos, 2.0, 3)
        pyglet.clock.schedule_once(self.b5.change_block_xpos, 3.0, -3)
        pyglet.clock.schedule_once(self.b5.change_block_ypos, 4.0, 2)
        pyglet.clock.schedule_once(self.b5.change_block_ypos, 5.0, -2)


    def loop2(self, dt):
        pyglet.clock.schedule_once(self.b4.set_block_colour, 0, arcade.csscolor.ALICE_BLUE)
        pyglet.clock.schedule_once(self.b4.set_block_colour, 1.0, arcade.csscolor.ANTIQUE_WHITE)
        pyglet.clock.schedule_once(self.b4.set_block_colour, 2.0, arcade.csscolor.AQUA)

    def destroy(self):
        pyglet.clock.unschedule(self.loop0)
        pyglet.clock.unschedule(self.loop1)
        pyglet.clock.unschedule(self.loop2)


def main():
    window = MyGame(width=12, height=12, title="Game")
    user_game = UserGame(window)
    window.setup_func = user_game.user_setup
    window.destroy_func = user_game.destroy
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

