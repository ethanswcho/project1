
def apply_arena(arena: str):



    return """
import arcade

# Constants
CHARACTER_SCALING = 1
TILE_SCALING = 0.5

# Size constants
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = int(SPRITE_PIXEL_SIZE * TILE_SCALING)

# Represents number of tiles for dimensions
HORIZONTAL_WIDTH = 12
VERTICAL_HEIGHT = 8

SCREEN_WIDTH = HORIZONTAL_WIDTH * GRID_PIXEL_SIZE
SCREEN_HEIGHT = VERTICAL_HEIGHT * GRID_PIXEL_SIZE

SCREEN_TITLE = "CPSC 410 - Project 1"

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 14


class MyGame(arcade.Window):

    def __init__(self):

        # Call the parent class and set up the window
        {}

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.wall_list = None
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

        # Create the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.game_over = False

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite(
            ":resources:images/animated_characters/zombie/zombie_idle.png", CHARACTER_SCALING)
        self.player_sprite.position = self.grid_to_pixels([0, 1])
        self.player_list.append(self.player_sprite)

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        self.create_default_ground()

        # Example coordinates to place crates on the ground
        # block_coordinate_list = [[2, 1],
        #                          [5, 1],
        #                          [7, 1]]

        # Create the 'physics engine'
        # First argument is the moving sprite, second argument is list of sprites that moving sprite cannot move through
        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                            self.wall_list,
                                                            GRAVITY)

    def set_goal_block(self, block):
        # Set block as the goal block. Spawns a flag on top of the block.
        block.color = arcade.csscolor.AQUA
        flag = arcade.Sprite(":resources:images/items/flagRed1.png", TILE_SCALING)
        flag.position = [block.position[0], block.position[1] + GRID_PIXEL_SIZE]
        self.goal = flag

    def on_draw(self):

        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.wall_list.draw()
        self.goal.draw()
        self.player_list.draw()

    def is_on_goal(self):
        if self.goal:
            return arcade.check_for_collision(self.player_sprite, self.goal)
        return False
        
    def on_key_press(self, key, modifiers):

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
        for x in range(0, HORIZONTAL_WIDTH):
            ground = arcade.Sprite(":resources:images/tiles/grassMid.png", TILE_SCALING)
            grid_position = self.grid_to_pixels([x, 0])
            ground.position = grid_position

            if (x == 0):
                ground.color = arcade.csscolor.GRAY

            # TODO: remove this when goal block can be set dynamically
            if (x == HORIZONTAL_WIDTH - 1):
                self.set_goal_block(ground)
            self.wall_list.append(ground)

    def on_key_release(self, key, modifiers):

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
        self.is_on_goal()
        
        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

    def process_keychange(self):

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

    def grid_to_pixels(self, coordinate):

        grid_position = [0, 0]
        grid_position[0] = coordinate[0] * \
            GRID_PIXEL_SIZE + (GRID_PIXEL_SIZE / 2)
        grid_position[1] = coordinate[1] * \
            GRID_PIXEL_SIZE + (GRID_PIXEL_SIZE / 2)
        return grid_position

    def add_static_blocks(self, block_coordinates):

        for coordinate in block_coordinates:
            self.add_static_block(coordinate)

    def add_static_block(self, coordinate):

        grid_position = self.grid_to_pixels(coordinate)
        block = arcade.Sprite(
            ":resources:images/tiles/grassMid.png", TILE_SCALING)
        block.position = grid_position
        self.wall_list.append(block)

    def set_horizontal_moving_block(self, start_x, start_y, boundary_left, boundary_right, change_x):

        block = arcade.Sprite(
            ":resources:images/tiles/dirtMid.png", TILE_SCALING)

        grid_position = self.grid_to_pixels([start_x, start_y])
        block.position = grid_position
        block.boundary_left = boundary_left * GRID_PIXEL_SIZE
        block.boundary_right = boundary_right * GRID_PIXEL_SIZE
        block.change_x = change_x * TILE_SCALING

        return block

    def set_vertical_moving_block(self, start_x, start_y, boundary_top, boundary_bottom, change_y):

        block = arcade.Sprite(
            ":resources:images/tiles/dirtMid.png", TILE_SCALING)

        grid_position = self.grid_to_pixels([start_x, start_y])
        block.position = grid_position
        block.boundary_top = boundary_top * GRID_PIXEL_SIZE
        block.boundary_bottom = boundary_bottom * GRID_PIXEL_SIZE
        block.change_y = change_y * TILE_SCALING

        return block

def main():

    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
        """.format(arena)