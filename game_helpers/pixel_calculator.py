# Constants
TILE_SCALING = 0.5
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = int(SPRITE_PIXEL_SIZE * TILE_SCALING)


def calculate_tile_to_pixel_displacement(tile_displacement):
    return (tile_displacement * GRID_PIXEL_SIZE) + (GRID_PIXEL_SIZE / 2)


def pixels_to_grid_point(pixels):
    return pixels / SPRITE_PIXEL_SIZE * TILE_SCALING


def grid_coord_to_pixels(coordinate):
    """
    Parameters
    ----------
    coordinate : list
        A coordinate [x, y] in tile location
    """

    grid_position = [0, 0]
    grid_position[0] = grid_point_to_pixels(coordinate[0])
    grid_position[1] = grid_point_to_pixels(coordinate[1])
    return grid_position


def grid_point_to_pixels(point):
    """
    Change a single point from tile to pixels
    """
    return point * GRID_PIXEL_SIZE + (GRID_PIXEL_SIZE / 2)
