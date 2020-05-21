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
DEFAULT_SCREEN_WIDTH = ARENA_WIDTH * GRID_PIXEL_SIZE
DEFAULT_SCREEN_HEIGHT = ARENA_HEIGHT * GRID_PIXEL_SIZE

DEFAULT_SCREEN_TITLE = "CPSC 410 - Project 1"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 15


class MyGame(arcade.Window):
    """
    Main application class.
        Optional inputs: "width", "height"
        "width": Arena width
        "height": Arena height
    """

    # Initializes first screen 
    def __init__(self, **args):

        # Call the parent class and set up the window
        SCREEN_WIDTH = DEFAULT_SCREEN_WIDTH
        SCREEN_HEIGHT = DEFAULT_SCREEN_HEIGHT
        TITLE = DEFAULT_SCREEN_TITLE
        if "width" in args:
            SCREEN_WIDTH = args["width"]
        if "height" in args:
            SCREEN_HEIGHT = args["height"]
        if "title" in args:
            SCREEN_TITLE = args["title"]

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = []
        self.block_list = []
        self.player_list = []
        self.moving_wall_list = []

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

        # Game properties
        self.goal = None
        self.game_over = False

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

        # Create the edge boundary
        self.create_edge_boundary()

        # Example coordinates to place crates on the ground
        # block_coordinate_list = [[2, 1],
        #                          [5, 1],
        #                          [7, 1]]

        # TODO: test code, remove from final code
        block1 = self.make_block([3, 3])
        block2 = self.make_block([6, 2])
        self.set_block_up_movement(block1, 2, 4)
        self.set_block_right_movement(block2, 2, 3)
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

        if self.game_over:
            self.draw_game_over()

    def is_on_goal(self):
        """ Check if the player is on a goal block """
        if self.goal is not None:
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
        elif key == arcade.key.SPACE and self.game_over:
            self.setup()

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

    def create_edge_boundary(self):
        # Creates the boundary walls
        for y in range(0, ARENA_HEIGHT):
            side_l = arcade.Sprite(
                ":resources:images/tiles/stoneCenter_rounded.png", TILE_SCALING)
            side_r = arcade.Sprite(
                ":resources:images/tiles/stoneCenter_rounded.png", TILE_SCALING)
            grid_position_l = self.grid_coord_to_pixels([-1, y])
            grid_position_r = self.grid_coord_to_pixels([ARENA_WIDTH, y])
            side_l.position = grid_position_l
            side_r.position = grid_position_r
            self.wall_list.append(side_l)
            self.wall_list.append(side_r)

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
        if not self.game_over:
            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.physics_engine.update()
            self.check_movement()
            if self.is_on_goal():
                self.end_game()

    def end_game(self):
        self.game_over = True

    def draw_game_over(self):
        win_message = "NOICE"
        arcade.draw_text(win_message, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.WHITE, 54, align="center",
                         anchor_x="center", anchor_y="bottom")

        restart_message = "Press space to restart"
        arcade.draw_text(restart_message, SCREEN_WIDTH/2, SCREEN_HEIGHT/2, arcade.color.WHITE, 16, align="center",
                         anchor_x="center", anchor_y="top")

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

    # Convert [x, y] in pixels to [x, y] in grid coordinates
    def pixels_to_grid_coord(self, pixels):
        """
        parameters
        ------------
        pixels: list
            Pixels [x, y]
        """

        grid_coord = [0,0]
        grid_coord[0] = self.pixels_to_grid_point(grid_coord[0])
        grid_coord[1] = self.pixels_to_grid_point(grid_coord[1])
    
    def pixels_to_grid_point(self, pixels):
        return pixels/SPRITE_PIXEL_SIZE*TILE_SCALING

    # Add blocks to the block_list
    def add_blocks(self, blocks):
        for block in blocks:
            self.wall_list.append(block)
            self.block_list.append(block)

    # Creates a block and sets its position to coordinate
    def make_block(self, coordinate):
        block = arcade.Sprite(
            ":resources:images/tiles/grassMid.png", TILE_SCALING)
        self.wall_list.append(block)
        self.block_list.append(block)
        self.set_block_position(block, coordinate)
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
        block.boundary_bottom = None
        block.boundary_top = None
        block.boundary_right = block.position[0] + \
            (displacement * GRID_PIXEL_SIZE) + (GRID_PIXEL_SIZE / 2)
        block.change_x = speed * TILE_SCALING

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
        block.boundary_bottom = None
        block.boundary_top = None
        block.boundary_left = block.position[0] - \
            (displacement * GRID_PIXEL_SIZE) - (GRID_PIXEL_SIZE / 2)
        block.change_x = -speed * TILE_SCALING

    # Moves a block to the up by displacement number of tiles at speed
    def set_block_up_movement(self, block, displacement, speed):
        """ 
        Parameters
        ----------
        block : arcade.Sprite
            The block to move
        displacement : int
            Number of tiles to move upwards
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert(speed > 0)
        block.boundary_bottom = None
        block.boundary_left = None
        block.boundary_right = None
        block.boundary_top = block.position[1] + \
            (displacement * GRID_PIXEL_SIZE) + (GRID_PIXEL_SIZE / 2)
        block.change_y = speed * TILE_SCALING

    # Moves a block to the up by displacement number of tiles at speed
    def set_block_down_movement(self, block, displacement, speed):
        """ 
        Parameters
        ----------
        block : arcade.Sprite
            The block to move
        displacement : int
            Number of tiles to move downwards
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert(speed > 0)
        block.boundary_top = None
        block.boundary_left = None
        block.boundary_right = None
        block.boundary_bottom = block.position[1] - \
            (displacement * GRID_PIXEL_SIZE) + (GRID_PIXEL_SIZE / 2)
        block.change_y = -speed * TILE_SCALING

    # Check all blocks in self.block_list and halt its movement if it has reached its boudary
    def check_movement(self):
        for block in self.block_list:
            if block.boundary_right is not None:
                if (block.center_x + GRID_PIXEL_SIZE / 2 >= block.boundary_right):
                    block.stop()

            elif block.boundary_left is not None:
                if (block.center_x - GRID_PIXEL_SIZE / 2 <= block.boundary_left):
                    block.stop()

            elif block.boundary_top is not None:
                if (block.center_y + GRID_PIXEL_SIZE / 2 >= block.boundary_top):
                    block.stop()

            elif block.boundary_bottom is not None:
                if (block.center_y - GRID_PIXEL_SIZE / 2 <= block.boundary_bottom):
                    block.stop()


def main():
    """ Main method """
    window = MyGame(width=12, height=8)
    """
    customizating methods (ex. block creation) come here
    """
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
