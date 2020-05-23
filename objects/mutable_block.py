import arcade
import game_helpers.pixel_calculator as pcalc


class MutableBlock(arcade.Sprite):

    def __init__(self, window: arcade.Window, name: str, coordinates: tuple, is_goal: bool = False):
        self.window = window
        self.flag = None
        self.name = name
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
            ":resources:images/items/flagRed1.png", pcalc.TILE_SCALING)
        flag.position = [self.position[0],
                         self.position[1] + pcalc.GRID_PIXEL_SIZE]
        self.flag = flag
        self.window.goal_list.append(flag)

    def set_block_position(self, coordinates):
        """
        Sets a block's position in tile position
        """
        grid_position = pcalc.grid_coord_to_pixels(coordinates)
        self.position = grid_position

    def set_block_right_movement(self, displacement, speed):
        """
        Moves a block to the right by displacement number of tiles at speed

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
        self.boundary_right = self.position[0] + pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_x = speed * pcalc.TILE_SCALING
        # TODO: Move the flag as well
        # self.window.goal_list.sprite_list[self.window.goal_list.sprite_list.index(self.flag)].change_x = speed * pcalc.TILE_SCALING

    def set_block_left_movement(self, displacement, speed):
        """
        Moves a block to the left by displacement number of tiles at speed

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
        self.boundary_left = self.position[0] - pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_x = -speed * pcalc.TILE_SCALING

    def set_block_up_movement(self, displacement, speed):
        """
        Moves a block to the up by displacement number of tiles at speed

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
        self.boundary_top = self.position[1] + pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_y = speed * pcalc.TILE_SCALING

    def set_block_down_movement(self, displacement, speed):
        """
        Moves a block to the up by displacement number of tiles at speed
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
        self.boundary_bottom = self.position[1] - pcalc.calculate_tile_to_pixel_displacement(displacement)
        self.change_y = -speed * pcalc.TILE_SCALING
