# Constants
BLOCK = "block"
GOAL = "goal"
DEFAULT_BLOCK_WIDTH = 1
DEFAULT_BLOCK_HEIGHT = 1


class Block:

    def __init__(self, block_type: str, x_pos: int, y_pos: int):
        self.type = block_type
        self.x = x_pos
        self.y = y_pos
