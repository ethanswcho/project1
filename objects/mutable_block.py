import arcade
import game_helpers.pixel_calculator as pcalc

# Constants for the flag sprite
FLAG_SPRITE_SCALING = 0.4
FLAG_RIGHT_SHIFT = 6
FLAG_DOWN_SHIFT = 10


class MutableBlock(arcade.Sprite):

    def __init__(self, window: arcade.Window, coordinates: tuple, is_goal: bool = False):
        self.window = window
        self.flag = None
        super().__init__(":resources:images/tiles/grassMid.png", pcalc.TILE_SCALING)
        window.wall_list.append(self)
        window.block_list.append(self)
        self.set_block_position(coordinates)
        if is_goal:
            self.set_goal_block()

    def set_goal_block(self):
        # Set block as the goal block. Spawns a flag on top of the block.
        self.color = arcade.csscolor.AQUA
        flag = arcade.Sprite(
            ":resources:images/items/flagRed1.png", FLAG_SPRITE_SCALING)
        flag.position = [self.position[0] + FLAG_RIGHT_SHIFT,
                         self.position[1] + pcalc.GRID_PIXEL_SIZE - FLAG_DOWN_SHIFT]
        self.flag = flag
        self.window.goal_list.append(flag)

    def set_block_position(self, coordinates):
        """
        Sets a block's position in tile position
        """
        grid_position = pcalc.grid_coord_to_pixels(coordinates)
        self.position = grid_position

    def set_block_xpos(self, dt,  coordinate):
        """
        Sets a block's xpos in tile position
        """
        self.position = [pcalc.grid_point_to_pixels(coordinate), self.position[1]]

    def set_block_ypos(self, dt, coordinate):
        """
        Sets a block's ypos in tile position
        """
        self.position = [self.position[0], pcalc.grid_point_to_pixels(coordinate)]


    def set_block_right_movement(self, dt, displacement, speed):
        """
        Moves a block to the right by displacement number of tiles at speed. 
        If the block is a goal_block, also set the flag's movement.

        Parameters
        ----------
        displacement : int
            Number of tiles to move to the right
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert (speed > 0)
        self.boundary_left = None
        self.boundary_bottom = None
        self.boundary_top = None
        self.boundary_right = self.position[0] + \
            pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_x = speed * pcalc.TILE_SCALING

        if self.flag is not None:
            self.flag.boundary_left = None
            self.flag.boundary_bottom = None
            self.flag.boundary_top = None
            self.flag.boundary_right = self.flag.position[0] + \
                pcalc.calculate_tile_to_pixel_displacement(displacement)
            self.flag.change_x = speed * pcalc.TILE_SCALING

    def set_block_left_movement(self, dt, displacement, speed):
        """
        Moves a block to the left by displacement number of tiles at speed.
        If the block is a goal_block, also set the flag's movement.

        Parameters
        ----------
        displacement : int
            Number of tiles to move to the left
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert (speed > 0)
        self.boundary_right = None
        self.boundary_bottom = None
        self.boundary_top = None
        self.boundary_left = self.position[0] - \
            pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_x = -speed * pcalc.TILE_SCALING

        if self.flag is not None:
            self.flag.boundary_right = None
            self.flag.boundary_bottom = None
            self.flag.boundary_top = None
            self.flag.boundary_left = self.flag.position[0] - \
                pcalc.calculate_tile_to_pixel_displacement(displacement)
            self.flag.change_x = -speed * pcalc.TILE_SCALING

    def set_block_up_movement(self, dt, displacement, speed):
        """
        Moves a block to the up by displacement number of tiles at speed.
        If the block is a goal_block, also set the flag's movement.

        Parameters
        ----------
        displacement : int
            Number of tiles to move upwards
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert (speed > 0)
        self.boundary_bottom = None
        self.boundary_left = None
        self.boundary_right = None
        self.boundary_top = self.position[1] + \
            pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_y = speed * pcalc.TILE_SCALING

        if self.flag is not None:
            self.flag.boundary_bottom = None
            self.flag.boundary_left = None
            self.flag.boundary_right = None
            self.flag.boundary_top = self.flag.position[1] + \
                pcalc.calculate_tile_to_pixel_displacement(displacement)
            self.flag.change_y = speed * pcalc.TILE_SCALING

    def set_block_down_movement(self, dt, displacement, speed):
        """
        Moves a block to the up by displacement number of tiles at speed.
        If the block is a goal_block, also set the flag's movement.

        Parameters
        ----------
        displacement : int
            Number of tiles to move downwards
        speed : int
            Speed at which the block moves. Must be positive.
        """
        assert (speed > 0)
        self.boundary_top = None
        self.boundary_left = None
        self.boundary_right = None
        self.boundary_bottom = self.position[1] - \
            pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_y = -speed * pcalc.TILE_SCALING

        if self.flag is not None:
            self.flag.boundary_top = None
            self.flag.boundary_left = None
            self.flag.boundary_right = None
            self.flag.boundary_bottom = self.flag.position[1] - \
                pcalc.calculate_tile_to_pixel_displacement(displacement)
            self.flag.change_y = -speed * pcalc.TILE_SCALING
