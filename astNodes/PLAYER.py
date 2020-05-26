from libs.node import Node

# Constants
DEFAULT_XPOS = 0
DEFAULT_YPOS = 1


class PLAYER(Node):

    def __init__(self):
        self.xpos = DEFAULT_XPOS
        self.ypos = DEFAULT_YPOS
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("put player")
        self.tokenizer.get_and_check_next("at")
        self.xpos = int(self.tokenizer.get_next())
        self.tokenizer.get_and_check_next(",")
        self.ypos = int(self.tokenizer.get_next())

    def evaluate(self):
        # Need to initialize physics engine here after player sprite is created
        return "".join((f"        self.player = PlayerSprite(self.window, ({self.xpos}, {self.ypos}))\n",
                        f"        self.window.physics_engine = arcade.PhysicsEnginePlatformer(",
                        f"self.player, self.window.wall_list, 1)\n"))
