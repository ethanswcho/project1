from libs.Node import Node

# Constants
DEFAULT_WIDTH = 1000
DEFAULT_HEIGHT = 650
SCREEN_TITLE = "Game"
BACKGROUND_COLOUR = "arcade.csscolor.CORNFLOWER_BLUE"


class ARENA(Node):

    def __init__(self):
        self.width = DEFAULT_WIDTH
        self.height = DEFAULT_HEIGHT
        self.title = SCREEN_TITLE
        self.background_colour = BACKGROUND_COLOUR
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("arena size")
        self.width = int(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next(",")
        self.height = int(self.tokenizer.get_next())

    def get_fields(self):
        return {
            "width": self.width,
            "height": self.height,
            "title": self.title,
            "background_color": self.background_colour
        }

    def evaluate(self):
        # TODO
        pass
