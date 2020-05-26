import math

# Constants
TILE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = int(SPRITE_PIXEL_SIZE * TILE_SCALING)


def calculate_tile_to_pixel_displacement(tile_displacement):
    return (tile_displacement * GRID_PIXEL_SIZE) + (GRID_PIXEL_SIZE / 2)


def grid_coord_to_pixels(coordinates: tuple):
    """
    Parameters
    ----------
    coordinates : list
        Coordinates (x, y) in tile location
    """
    return grid_point_to_pixels_offset(coordinates[0]), grid_point_to_pixels_offset(coordinates[1])


def grid_point_to_pixels_offset(point):
    """
    Change a single point from tile to pixels with middle offset
    """
    return point * GRID_PIXEL_SIZE + math.copysign(1.0, point) * (GRID_PIXEL_SIZE / 2)


def grid_point_to_pixels(point):
    """
        Change a single point from tile to pixels without middle offset
        """
    return point * GRID_PIXEL_SIZE
