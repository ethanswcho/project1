import arcade
import game_helpers.pixel_calculator as pcalc


class SpriteWrapper(arcade.Sprite):

    def __init__(self, window: arcade.Window, coordinates: tuple, image: str, scaling: float=1.0):
        self.window = window
        super().__init__(image, scaling)
        self.set_start_position(coordinates)

    def set_start_position(self, coordinates):
        """
        Sets a block's position in tile position
        """
        grid_position = pcalc.grid_coord_to_pixels(coordinates)
        self.position = grid_position
