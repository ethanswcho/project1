"""
Platformer Game
"""
import arcade
import game_helpers.pixel_calculator as pcalc

# Constants
CHARACTER_SCALING = 0.6

# Represents dimensions of the arena in tiles
ARENA_WIDTH = 12
ARENA_HEIGHT = 8

# Represents the default arena fields
DEFAULT_SCREEN_WIDTH = ARENA_WIDTH * pcalc.GRID_PIXEL_SIZE
DEFAULT_SCREEN_HEIGHT = ARENA_HEIGHT * pcalc.GRID_PIXEL_SIZE
DEFAULT_SCREEN_TITLE = "CPSC 410 - Project 1"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 18


class MyGame(arcade.Window):
    """
    Main application class.
        Input: "setup_func"
        Optional inputs: "width", "height"
        "setup_func": the user defined game setup method to call when restarting
        "width": Arena width
        "height": Arena height
    """

    # Initializes first screen 
    def __init__(self, **args):

        self.setup_func = args["setup_func"]
        self.screen_width = DEFAULT_SCREEN_WIDTH
        self.screen_height = DEFAULT_SCREEN_HEIGHT
        self.title = DEFAULT_SCREEN_TITLE

        # Call the parent class and set up the window
        if "width" in args:
            self.screen_width = args["width"] * pcalc.GRID_PIXEL_SIZE
        if "height" in args:
            self.screen_height = args["height"] * pcalc.GRID_PIXEL_SIZE
        if "title" in args:
            self.title = args["title"] * pcalc.GRID_PIXEL_SIZE

        super().__init__(self.screen_width, self.screen_height, self.title)

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
        self.player_sprite.position = [0, pcalc.grid_point_to_pixels(1)]
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        self.create_default_ground()

        # Create the edge boundary
        self.create_edge_boundary()

        # TODO: test code, remove from final code
        block1 = self.make_block([3, 3])
        block2 = self.make_block([6, 2])
        self.set_block_up_movement(block1, 2, 4)
        self.set_block_right_movement(block2, 2, 3)

        # Create the 'physics engine'
        # First argument is the moving sprite, second argument is list of sprites that moving sprite cannot move through
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list, GRAVITY)
        self.setup_func(self)

    def set_goal_block(self, block):
        # Set block as the goal block. Spawns a flag on top of the block.
        block.color = arcade.csscolor.AQUA
        flag = arcade.Sprite(
            ":resources:images/items/flagRed1.png", pcalc.TILE_SCALING)
        flag.position = [block.position[0],
                         block.position[1] + pcalc.GRID_PIXEL_SIZE]
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

        self.process_key_change()

    def create_default_ground(self):
        # Creates the layer of ground for each level
        for x in range(0, ARENA_WIDTH):
            ground = arcade.Sprite(
                ":resources:images/tiles/grassMid.png", pcalc.TILE_SCALING)
            grid_position = pcalc.grid_coord_to_pixels([x, 0])
            ground.position = grid_position

            # TODO: test code to make grid clearer
            if x % 2 == 0:
                ground.color = arcade.csscolor.PALE_TURQUOISE

            if x == 0:
                ground.color = arcade.csscolor.GRAY

            # TODO: remove this when goal block can be set dynamically
            if x == ARENA_WIDTH - 1:
                self.set_goal_block(ground)
            self.wall_list.append(ground)

    def create_edge_boundary(self):
        # Creates the boundary walls
        for y in range(0, ARENA_HEIGHT):
            side_l = arcade.Sprite(
                ":resources:images/tiles/stoneCenter_rounded.png", pcalc.TILE_SCALING)
            side_r = arcade.Sprite(
                ":resources:images/tiles/stoneCenter_rounded.png", pcalc.TILE_SCALING)
            grid_position_l = pcalc.grid_coord_to_pixels([-1, y])
            grid_position_r = pcalc.grid_coord_to_pixels([ARENA_WIDTH, y])
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

        self.process_key_change()

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
        arcade.draw_text(win_message, self.screen_width/2, self.screen_height/2, arcade.color.WHITE, 54,
                         align="center", anchor_x="center", anchor_y="bottom")

        restart_message = "Press space to restart"
        arcade.draw_text(restart_message, self.screen_width/2, self.screen_height/2, arcade.color.WHITE, 16,
                         align="center", anchor_x="center", anchor_y="top")

    def process_key_change(self):
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

    # Add blocks to the block_list
    def add_blocks(self, blocks):
        for block in blocks:
            self.wall_list.append(block)
            self.block_list.append(block)

    # Creates a block and sets its position to coordinate
    def make_block(self, coordinate):
        block = arcade.Sprite(
            ":resources:images/tiles/grassMid.png", pcalc.TILE_SCALING)
        self.wall_list.append(block)
        self.block_list.append(block)
        self.set_block_position(block, coordinate)
        return block

    # Sets a block's position in tile position
    def set_block_position(self, block, coordinate):
        grid_position = pcalc.grid_coord_to_pixels(coordinate)
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
        block.boundary_right = block.position[0] + pcalc.calculate_tile_to_pixel_displacement(displacement)
        block.change_x = speed * pcalc.TILE_SCALING

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
        block.boundary_left = block.position[0] - pcalc.calculate_tile_to_pixel_displacement(displacement)
        block.change_x = -speed * pcalc.TILE_SCALING

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
        block.boundary_top = block.position[1] + pcalc.calculate_tile_to_pixel_displacement(displacement)
        block.change_y = speed * pcalc.TILE_SCALING

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
        block.boundary_bottom = block.position[1] - pcalc.calculate_tile_to_pixel_displacement(displacement)
        block.change_y = -speed * pcalc.TILE_SCALING

    # Check all blocks in self.block_list and halt its movement if it has reached its boudary
    def check_movement(self):
        for block in self.block_list:
            if block.boundary_right is not None:
                if block.center_x + pcalc.GRID_PIXEL_SIZE / 2 >= block.boundary_right:
                    block.stop()

            elif block.boundary_left is not None:
                if block.center_x - pcalc.GRID_PIXEL_SIZE / 2 <= block.boundary_left:
                    block.stop()

            elif block.boundary_top is not None:
                if block.center_y + pcalc.GRID_PIXEL_SIZE / 2 >= block.boundary_top:
                    block.stop()

            elif block.boundary_bottom is not None:
                if block.center_y - pcalc.GRID_PIXEL_SIZE / 2 <= block.boundary_bottom:
                    block.stop()
