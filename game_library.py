"""
Platformer Game
"""
import arcade
import game_helpers.pixel_calculator as pcalc

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
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
        self.setup_func = None
        self.destroy_func = None
        self.screen_width = args["width"]
        self.screen_width_pixels = self.screen_width * pcalc.GRID_PIXEL_SIZE
        self.screen_height = args["height"]
        self.screen_height_pixels = self.screen_height * pcalc.GRID_PIXEL_SIZE
        self.title = args["title"]

        super().__init__(self.screen_width_pixels, self.screen_height_pixels, self.title)

        # These are 'lists' that keep track of our sprites. Each sprite should
        # go into a list.
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()

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
        # Clear the Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.block_list = arcade.SpriteList()
        self.goal_list = arcade.SpriteList()

        self.game_over = False

        # Create the ground
        # This shows using a loop to place multiple sprites horizontally
        self.create_default_ground()

        # Create the edge boundary
        self.create_edge_boundary()

        self.setup_func()

    def set_field(self, field, value):
        setattr(self, field, value)

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen to the background color
        arcade.start_render()

        # Draw our sprites
        self.goal_list.draw()
        self.wall_list.draw()
        self.player_list.draw()

        if self.game_over:
            self.draw_game_over()

    def is_on_goal(self):
        """ Check if the player is on a goal block """
        if len(self.goal_list) != 0:
            return arcade.check_for_collision_with_list(self.player_sprite, self.goal_list)
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
        for x in range(0, self.screen_width):
            ground = arcade.Sprite(
                ":resources:images/tiles/grassMid.png", pcalc.TILE_SCALING)
            grid_position = pcalc.grid_coord_to_pixels((x, 0))
            ground.position = grid_position

            # TODO: test code to make grid clearer
            if x == 0:
                ground.color = arcade.csscolor.GRAY
            elif x % 2 == 0:
                ground.color = arcade.csscolor.PALE_TURQUOISE

            self.wall_list.append(ground)

    def create_edge_boundary(self):
        # Creates the boundary walls
        for y in range(0, self.screen_height):
            side_l = arcade.Sprite(
                ":resources:images/tiles/stoneCenter_rounded.png", pcalc.TILE_SCALING)
            side_r = arcade.Sprite(
                ":resources:images/tiles/stoneCenter_rounded.png", pcalc.TILE_SCALING)
            grid_position_l = pcalc.grid_coord_to_pixels((-0.0, y))
            grid_position_r = pcalc.grid_coord_to_pixels((self.screen_width, y))
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
            # Call update on all sprites
            self.physics_engine.update()
            self.check_movement()
            # Update all the goals
            for goal in self.goal_list:
                goal.update()
            if self.is_on_goal():
                self.end_game()

    def end_game(self):
        self.game_over = True
        self.destroy_func()

    def draw_game_over(self):
        win_message = "NOICE"
        arcade.draw_text(win_message, self.screen_width_pixels/2, self.screen_height_pixels/2,
                         arcade.color.WHITE, 54, align="center", anchor_x="center", anchor_y="bottom")

        restart_message = "Press space to restart"
        arcade.draw_text(restart_message, self.screen_width_pixels/2, self.screen_height_pixels/2,
                         arcade.color.WHITE, 16, align="center", anchor_x="center", anchor_y="top")

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

    def check_movement(self):
        """
        Check all blocks in self.block_list and goals in self.goal_list and halts 
        their movement if they have reached their boundaries.
        """

        # Combine the list of goals and blocks into one list
        combined_sprite_list = arcade.SpriteList()
        combined_sprite_list.extend(self.goal_list)
        combined_sprite_list.extend(self.block_list)

        for sprite in combined_sprite_list:
            if sprite.boundary_right is not None:
                if sprite.center_x + pcalc.GRID_PIXEL_SIZE / 2 >= sprite.boundary_right:
                    sprite.stop()

            elif sprite.boundary_left is not None:
                if sprite.center_x - pcalc.GRID_PIXEL_SIZE / 2 <= sprite.boundary_left:
                    sprite.stop()

            elif sprite.boundary_top is not None:
                if sprite.center_y + pcalc.GRID_PIXEL_SIZE / 2 >= sprite.boundary_top:
                    sprite.stop()

            elif sprite.boundary_bottom is not None:
                if sprite.center_y - pcalc.GRID_PIXEL_SIZE / 2 <= sprite.boundary_bottom:
                    sprite.stop()
