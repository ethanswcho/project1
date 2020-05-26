from libs.node import Node


class REMOVESTATEMENT(Node):

    def __init__(self):
        self.block_name = None
        super().__init__()

    def parse(self):
        self.tokenizer.get_and_check_next("destroy")
        self.block_name = self.tokenizer.get_next()
        if self.block_name == "player":
            raise Exception("Cannot remove player")

    def evaluate(self, wait=0):
        return f"        pyglet.clock.schedule_once(lambda dt: self.{self.block_name}.kill(), {wait})"
