"""
Platformer Game
"""
import arcade

# Constants
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Size constants
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = int(SPRITE_PIXEL_SIZE * TILE_SCALING)

# Represents dimensions of the arena in tiles
ARENA_WIDTH = 12
ARENA_HEIGHT = 8

# Represents the dimensions of the arena in pixels
SCREEN_WIDTH = ARENA_WIDTH * GRID_PIXEL_SIZE
SCREEN_HEIGHT = ARENA_HEIGHT * GRID_PIXEL_SIZE

SCREEN_TITLE = "CPSC 410 - Project 1"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 14


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
        self.block_list = None
        self.player_list = None
        self.moving_wall_list = None

        # Track the current state of what key is pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()

        self.game_over = False

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/zombie/zombie_idle.png", CHARACTER_SCALING)
        self.player_sprite.position = self.grid_coord_to_pixels([0, 1])
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        self.create_default_ground()

        # Example coordinates to place crates on the ground
        # block_coordinate_list = [[2, 1],
        #                          [5, 1],
        #                          [7, 1]]

        # TODO: test code, remove from final code
        # block1 = self.make_block()
        # block2 = self.make_block()
        # self.set_block_position(block1, [5, 1])
        # self.set_block_position(block2, [6, 2])
        # self.set_block_right_movement(block2, 2, 3)
        # self.set_block_left_movement(block1, 2, 3)

        # Create the 'physics engine'
        # First argument is the moving sprite, second argument is list of sprites that moving sprite cannot move through
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             GRAVITY)

    def set_goal_block(self, block):
        # Set block as the goal block. Spawns a flag on top of the block.
        block.color = arcade.csscolor.AQUA
        flag = arcade.Sprite(
            ":resources:images/items/flagRed1.png", TILE_SCALING)
        flag.position = [block.position[0],
                         block.position[1] + GRID_PIXEL_SIZE]
        self.goal = flag

    def on_draw(self):
        """ Render the screen. """

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.goal.draw()
        self.player_list.draw()

    def is_on_goal(self):
        """ Check if the player is on a goal block """
        if self.goal:
            return arcade.check_for_collision(self.player_sprite, self.goal)
        return False

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        self.process_keychange()

    def create_default_ground(self):
        # Creates the layer of ground for each level
        for x in range(0, ARENA_WIDTH):
            ground = arcade.Sprite(
                ":resources:images/tiles/grassMid.png", TILE_SCALING)
            grid_position = self.grid_coord_to_pixels([x, 0])
            ground.position = grid_position

            # TODO: test code to make grid clearer
            if (x % 2 == 0):
                ground.color = arcade.csscolor.PALE_TURQUOISE

            if (x == 0):
                ground.color = arcade.csscolor.GRAY

            # TODO: remove this when goal block can be set dynamically
            if (x == ARENA_WIDTH - 1):
                self.set_goal_block(ground)
            self.wall_list.append(ground)

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()

    def update(self, delta_time):
        """ Movement and game logic """
        self.is_on_goal()

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.check_movement()

    def process_keychange(self):
        """
        Called when we change a key up/down or we move on/off a ladder.
        """
        # Process up/down
        if self.up_pressed and not self.down_pressed:
            if self.physics_engine.can_jump() and not self.jump_needs_reset:
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
                self.jump_needs_reset = True
        elif self.down_pressed and not self.up_pressed:
            if self.physics_engine.is_on_ladder():
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def grid_coord_to_pixels(self, coordinate):
        """ 
        Parameters
        ----------
        coordinate : list
            A coordinate [x, y] in tile location
        """

        grid_position = [0, 0]
        grid_position[0] = self.grid_point_to_pixels(coordinate[0])
        grid_position[1] = self.grid_point_to_pixels(coordinate[1])
        return grid_position

    # Change a single point from tile to pixels
    def grid_point_to_pixels(self, point):
        return point * GRID_PIXEL_SIZE + (GRID_PIXEL_SIZE / 2)

    # Add blocks to the block_list
    def add_blocks(self, blocks):
        for block in blocks:
            self.wall_list.append(block)
            self.block_list.append(block)

    # Creates a block and sets its position to coordinate
    def make_block(self):
        block = arcade.Sprite(
            ":resources:images/tiles/grassMid.png", TILE_SCALING)
        self.wall_list.append(block)
        self.block_list.append(block)
        return block

    # Sets a block's position in tile position
    def set_block_position(self, block, coordinate):
        grid_position = self.grid_coord_to_pixels(coordinate)
        block.position = grid_position

    # Moves a block to the right by displacement number of tiles at speed
    def set_block_right_movement(self, block, displacement, speed):
        """ 
        Parameters
        ----------
        block : arcade.Sprite
            The block to move
        displacement : int
            Number of tiles to move to the right
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert(speed > 0)
        block.boundary_left = None
        block.boundary_right = block.position[0] + \
            (displacement * GRID_PIXEL_SIZE) + (GRID_PIXEL_SIZE / 2)
        block._set_change_x(speed * TILE_SCALING)

    # Moves a block to the right by displacement number of tiles at speed
    def set_block_left_movement(self, block, displacement, speed):
        """ 
        Parameters
        ----------
        block : arcade.Sprite
            The block to move
        displacement : int
            Number of tiles to move to the left
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert(speed > 0)
        block.boundary_right = None
        block.boundary_left = block.position[0] - \
            (displacement * GRID_PIXEL_SIZE) - + (GRID_PIXEL_SIZE / 2)
        block._set_change_x(-speed * TILE_SCALING)

    # Check all blocks in self.block_list and halt its movement if it has reached its boudary
    def check_movement(self):
        for block in self.block_list:
            if (block.boundary_right is not None):
                if (block.center_x + GRID_PIXEL_SIZE / 2 >= block.boundary_right):
                    block.stop()

            if (block.boundary_left is not None):
                if (block.center_x - GRID_PIXEL_SIZE / 2 <= block.boundary_left):
                    block.stop()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
