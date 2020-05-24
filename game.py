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
        arcade.schedule(self.loop0, 6.0)
        arcade.schedule(self.loop1, 2.0)

    def loop0(self, dt):
        pyglet.clock.schedule_once(self.b5.set_block_xpos, 0, 8)
        pyglet.clock.schedule_once(self.b5.set_block_ypos, 1.0, 8)
        pyglet.clock.schedule_once(self.b5.set_block_right_movement, 2.0, 2, 10)
        pyglet.clock.schedule_once(self.b5.set_block_up_movement, 3.0, 2, 10)
        pyglet.clock.schedule_once(self.b5.set_block_left_movement, 4.0, 2, 10)
        pyglet.clock.schedule_once(self.b5.set_block_down_movement, 5.0, 2, 10)


    def loop1(self, dt):
        pyglet.clock.schedule_once(lambda dt: setattr(self, 'b8', MutableBlock(self.window, (4, 7))), 0)
        pyglet.clock.schedule_once(lambda dt: self.b8.kill(), 1.0)

    def destroy(self):
        pyglet.clock.unschedule(self.loop0)
        pyglet.clock.unschedule(self.loop1)


def main():
    window = MyGame(width=12, height=12, title="Game")
    user_game = UserGame(window)
    window.setup_func = user_game.user_setup
    window.destroy_func = user_game.destroy
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()

