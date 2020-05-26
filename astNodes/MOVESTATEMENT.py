from libs.node import Node

# Constants
MOVE_SPEED = 10


class MOVESTATEMENT(Node):

    def __init__(self):
        self.block_name = None
        self.direction = None
        self.value = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("move")
        self.block_name = self.tokenizer.get_next()
        self.direction = self.tokenizer.get_and_check_next("up|down|left|right")
        self.tokenizer.get_and_check_next("by")
        self.value = int(self.tokenizer.get_next())

    def evaluate(self, wait=0):
        return "".join((f"        pyglet.clock.schedule_once(",
                        f"lambda dt: self.{self.block_name}.set_block_{self.direction}_movement(",
                        f"dt, {self.value}, {MOVE_SPEED}), {wait})"))
