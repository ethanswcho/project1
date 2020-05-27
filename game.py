from game_library import MyGame
from objects.mutable_block import MutableBlock
from objects.player_sprite import PlayerSprite
import arcade
import pyglet


class UserGame:

    def __init__(self, window: arcade.Window):
        self.window = window
        
    def user_setup(self):
        self.player = PlayerSprite(self.window, (2, 3))
        self.window.physics_engine = arcade.PhysicsEnginePlatformer(self.player, self.window.wall_list, 1)
        self.g1 = MutableBlock(self.window, (11, 1), is_goal=True)
        self.g2 = MutableBlock(self.window, (1, 4), is_goal=True)
        self.b2 = MutableBlock(self.window, (2, 2))
        self.b3 = MutableBlock(self.window, (3, 3))
        self.b4 = MutableBlock(self.window, (4, 4))
        self.b5 = MutableBlock(self.window, (5, 5))
        self.b6 = MutableBlock(self.window, (6, 6))
        self.b7 = MutableBlock(self.window, (7, 7))
        pyglet.clock.schedule_once(lambda dt: self.b6.set_block_right_movement(dt, 2, 10), 0)
        pyglet.clock.schedule_once(lambda dt: self.b3.set_block_xpos(dt, 8), 0)
        pyglet.clock.schedule_once(lambda dt: self.b3.change_block_xpos(dt, -4), 0)
        pyglet.clock.schedule_once(lambda dt: self.b7.kill(), 0)
        arcade.schedule(self.loop0, 2.0)
        arcade.schedule(self.loop1, 5.0)
        arcade.schedule(self.loop2, 6.0)

    def loop0(self, dt):
        pyglet.clock.schedule_once(lambda dt: self.b4.set_block_right_movement(dt, 2, 10), 0)
        pyglet.clock.schedule_once(lambda dt: self.b4.set_block_left_movement(dt, 2, 10), 1.0)


    def loop1(self, dt):
        pyglet.clock.schedule_once(lambda dt: setattr(self, 'b8', MutableBlock(self.window, (4, 7), is_goal=True)), 0)
        pyglet.clock.schedule_once(lambda dt: self.b8.set_block_up_movement(dt, 2, 10), 1.0)
        pyglet.clock.schedule_once(lambda dt: self.b8.set_block_ypos(dt, 7), 2.0)
        pyglet.clock.schedule_once(lambda dt: self.b8.change_block_xpos(dt, 4), 3.0)
        pyglet.clock.schedule_once(lambda dt: self.b8.kill(), 4.0)


    def loop2(self, dt):
        pyglet.clock.schedule_once(lambda dt: self.b5.set_block_xpos(dt, 8), 0)
        pyglet.clock.schedule_once(lambda dt: self.b5.set_block_ypos(dt, 8), 1.0)
        pyglet.clock.schedule_once(lambda dt: self.b5.change_block_xpos(dt, 3), 2.0)
        pyglet.clock.schedule_once(lambda dt: self.b5.change_block_xpos(dt, -3), 3.0)
        pyglet.clock.schedule_once(lambda dt: self.b5.change_block_ypos(dt, 2), 4.0)
        pyglet.clock.schedule_once(lambda dt: self.b5.change_block_ypos(dt, -2), 5.0)

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

