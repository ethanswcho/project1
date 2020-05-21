# Constants
BLOCK = "block"
GOAL = "goal"
DEFAULT_BLOCK_WIDTH = 10
DEFAULT_BLOCK_HEIGHT = 10


class Block:

    def __init__(self, block_type: str, x_pos: int, y_pos: int, block_width=None, block_height=None):
        self.type = block_type
        self.x = x_pos
        self.y = y_pos

        if block_width is not None:
            self.width = block_width
        else:
            self.width = DEFAULT_BLOCK_WIDTH

        if block_height is not None:
            self.height = block_height
        else:
            self.height = DEFAULT_BLOCK_HEIGHT

