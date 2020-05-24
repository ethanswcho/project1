from game_library import MyGame
from objects.mutable_block import MutableBlock
from pyglet import clock
import arcade

from functools import partial

def user_setup(window):
    MutableBlock(window, "g1", (11, 1), is_goal=True)
    MutableBlock(window, "g2", (1, 4), is_goal=True)
    MutableBlock(window, "b2", (2, 2))
    MutableBlock(window, "b3", (3, 3))
    MutableBlock(window, "b4", (4, 4))
    MutableBlock(window, "b5", (5, 5))
    MutableBlock(window, "b6", (6, 6))
    MutableBlock(window, "b7", (7, 7))

window = MyGame(setup_func=user_setup, width=12, height=12, title="Game")

def main():
    window.setup()
    do_loops()
    arcade.run()
   

def do_loops():
    arcade.schedule(loop1, 4)
    arcade.schedule(loop2, 4)

def loop1(self):
    print("loop1")
    window.get_block("b2").set_block_up_movement(2, 4)
    #clock.schedule_once(self.window.get_block("b2").set_block_right_movement(2, 4), 2)
    clock.sleep(200)
    window.get_block("b2").set_block_left_movement(2, 3)

def loop2(self):
    print("loop2")
    window.get_block("b3").set_block_up_movement(2, 1)
    

if __name__ == "__main__":
    main()

